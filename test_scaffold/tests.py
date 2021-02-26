# Python Standard Library Imports
import re

# Django Imports
# https://docs.djangoproject.com/en/1.11/topics/testing/overview/#provided-test-case-classes
from django.test import TestCase
from django.test.client import Client
from django.urls import (
    NoReverseMatch,
    reverse,
)
#from django.utils import unittest
from django.utils.http import urlencode

# HTK Imports
from htk.test_scaffold.constants import TESTSERVER
from htk.test_scaffold.models import TestScaffold
from htk.test_scaffold.utils import (
    create_test_email,
    create_test_password,
    create_test_user,
)


class BaseTestCase(TestCase):
    """Base class for all test cases
    """
    fixtures = ['initial_data',]

    def setUp(self):
        self.assigned_users = 0
        self.users = []
        self._create_batch_test_users()

    def _create_batch_test_users(self):
        for x in range(5):
            self.users.append(create_test_user())

    def _assign_test_user(self):
        """Returns:
        a user previously not returned
        """
        if self.assigned_users >= len(self.users):
            self._create_batch_test_users()
        user = self.users[self.assigned_users - 1]
        self.assigned_users += 1
        return user

class BaseWebTestCase(BaseTestCase):
    """Base class for other Web test cases
    Sets up some commonly-used parameters
    """
    fixtures = ['initial_data',]

    def setUp(self):
        super(BaseWebTestCase, self).setUp()
        # disable prelaunch mode for unit tests
        TestScaffold.set_fake_prelaunch(prelaunch_mode=False, prelaunch_host=False)

    def _get_user_session(self):
        """Returns an authenticated user, its password, and authenticated client
        """
        user = self._assign_test_user()
        password = create_test_password()
        user.set_password(password)
        user.save()
        client = Client()
        success = client.login(username=user.username, password=password)
        self.assertTrue(success)
        return (user, password, client,)

    def _get_user_session_with_primary_email(self):
        """Returns an authenticated user, its primary email, password, and authenticated client
        """
        (user, password, client,) = self._get_user_session()
        from htk.apps.accounts.utils import associate_user_email
        email = create_test_email()
        user_email = associate_user_email(user, email, confirmed=True)
        user_email.set_primary_email()
        return (user, email, password, client,)

    def _get(self, view_name, client=None, params=None, follow=False, view_args=None, view_kwargs=None, secure=False, **extra):
        """Wrapper for performing an HTTP GET request
        """
        params = {} if params is None else params
        view_args = [] if view_args is None else view_args
        view_kwargs = {} if view_kwargs is None else view_kwargs
        path = reverse(view_name, args=view_args, kwargs=view_kwargs)
        if type(client) != Client:
            client = Client()

        response = client.get(path, data=params, follow=follow, secure=secure, **extra)
        return response

    def _post(self, view_name, client=None, params=None, get_params=None, follow=False, view_args=None, view_kwargs=None, secure=False, **extra):
        """Wrapper for performing an HTTP POST request
        """
        params = {} if params is None else params
        get_params = {} if get_params is None else get_params
        view_args = [] if view_args is None else view_args
        view_kwargs = {} if view_kwargs is None else view_kwargs
        path = reverse(view_name, args=view_args, kwargs=view_kwargs)
        if get_params:
            query_string = urlencode(get_params)
            path = '%s?%s' % (path, query_string,)

        if type(client) != Client:
            client = Client()
        response = client.post(path, data=params, follow=follow, secure=secure, **extra)
        return response

    def _put(self, view_name, client=None, params=None, follow=False, view_args=None, view_kwargs=None, secure=False, **extra):
        """Wrapper for performing an HTTP PUT request
        """
        params = {} if params is None else params
        view_args = [] if view_args is None else view_args
        view_kwargs = {} if view_kwargs is None else view_kwargs
        path = reverse(view_name, args=view_args, kwargs=view_kwargs)
        if type(client) != Client:
            client = Client()

        response = client.put(path, data=params, follow=follow, secure=secure, **extra)
        return response

    def _delete(self, view_name, client=None, params=None, get_params=None, follow=False, view_args=None, view_kwargs=None, secure=False, **extra):
        """Wrapper for performing an HTTP DELETE request
        """
        params = {} if params is None else params
        get_params = {} if get_params is None else get_params
        view_args = [] if view_args is None else view_args
        view_kwargs = {} if view_kwargs is None else view_kwargs
        path = reverse(view_name, args=view_args, kwargs=view_kwargs)
        if get_params:
            query_string = urlencode(get_params)
            path = '%s?%s' % (path, query_string,)

        if type(client) != Client:
            client = Client()
        response = client.delete(path, data=params, follow=follow, secure=secure, **extra)
        return response

    def _check_view_is_okay(self, view_name, client=None, params=None, follow=False, secure=False):
        response = self._get(view_name, client=client, params=params, follow=follow, secure=secure)
        self.assertEqual(200,
                         response.status_code,
                         '[%s] got unexpected response code %d' %
                         (view_name,
                          response.status_code))

    def _check_view_does_not_exist(self, view_name, client=None, params=None, follow=False, message='View should not exist'):
        try:
            response = self._get(view_name, client=client, params=params, follow=follow)
        except NoReverseMatch:
            response = None
        self.assertIsNone(response, message)

    def _check_view_404(self, view_name, client=None, params=None, follow=False):
        response = self._get(view_name, client=client, params=params, follow=follow)
        self.assertEqual(404, response.status_code)

    def _check_response_redirect_chain_empty(self, view_name, response, extra_message=''):
        """Checks that response.redirect_chain is empty
        """
        redirect_chain = response.redirect_chain
        self.assertEqual(0,
                         len(redirect_chain),
                         'Unexpected redirect, should have stayed on [%s]. %s' % (view_name, extra_message,))

    def _check_response_redirect_chain(
        self,
        view_name,
        another,
        response,
        extra_message='',
        secure=False,
        redirect_chain_offset=-1,
        **kwargs
    ):
        """Check that response.redirect_chain is behaving correctly
        """
        redirect_chain = response.redirect_chain
        self.assertTrue(
            len(redirect_chain) > 0,
            '[%s] did not redirect to [%s]. %s' % (view_name, another, extra_message,)
        )
        self.assertEqual(302, redirect_chain[0][1])

        actual = redirect_chain[redirect_chain_offset][0]

        protocol_pattern = r'^https://' if secure else r'^http://'
        if re.match(protocol_pattern, another):
            # `another` is a full uri
            pattern = another
            match = re.match(pattern, actual)
        else:
            # `another` is a view name

            reversed_url = reverse(another)
            protocol_pattern = protocol_pattern + '%s%s'
            pattern = protocol_pattern % (TESTSERVER, reversed_url,)

            match = re.match(pattern, actual)

            if match is None:
                # https://docs.djangoproject.com/en/3.1/releases/1.9/#http-redirects-no-longer-forced-to-absolute-uris
                # make another attempt to check against the partial URI
                match = re.match(reversed_url, actual)

        self.assertIsNotNone(
            match,
            '[%s] redirected to [%s] instead of [%s][%s]' % (
                view_name,
                actual,
                another,
                pattern
            )
        )

    def _check_view_redirects_to_another(
        self,
        view_name,
        another,
        client=None,
        params=None,
        view_args=None,
        view_kwargs=None,
        method='get',
        secure=True,
        **kwargs
    ):
        """Perform an HTTP request and check that the redirect_chain behaves correctly for a page that is expected to redirect
        """
        if method == 'get':
            response = self._get(view_name, client=client, params=params, view_args=view_args, view_kwargs=view_kwargs, follow=True, secure=secure)
        elif method == 'post':
            response = self._post(view_name, client=client, params=params, view_args=view_args, view_kwargs=view_kwargs, follow=True, secure=secure)
        else:
            raise Exception('Unknown HTTP method: %s' % method)
        self._check_response_redirect_chain(
            view_name,
            another,
            response,
            secure=secure,
            **kwargs
        )

    def _check_view_redirects_to_login(
        self,
        view_name,
        client=None,
        login_url_name='account_login',
        secure=True
    ):
        self._check_view_redirects_to_another(
            view_name,
            login_url_name,
            client=client,
            secure=secure
        )

    def _check_prelaunch_mode(self, view_name):
        from htk.apps.prelaunch.utils import get_prelaunch_url_name
        prelaunch_url_name = get_prelaunch_url_name()
        self._check_view_redirects_to_another(view_name, get_prelaunch_url_name())

    def test_basic(self):
        self.assertTrue(True)
