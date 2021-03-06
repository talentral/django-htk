# Django Imports
from django.contrib import admin
from django.utils.safestring import mark_safe

# HTK Imports
from htk.apps.customers.models import (
    CustomerAttribute,
    OrganizationCustomerAttribute,
)
from htk.utils import (
    htk_setting,
    resolve_model_dynamically,
)


class CustomerAttributeInline(admin.TabularInline):
    model = CustomerAttribute
    extra = 0
    can_delete = True

class OrganizationCustomerAttributeInline(admin.TabularInline):
    model = OrganizationCustomerAttribute
    extra = 0
    can_delete = True

class BaseCustomerAdmin(admin.ModelAdmin):
    list_display = (
        'id',
        'user',
        'organization',
        'name',
        'attention',
        'email',
        'address',
        'mailing_address',
    )
    list_filter = (
        'organization',
    )
    inlines = (
        CustomerAttributeInline,
    )
    search_fields = (
        'name',
    )

class BaseOrganizationCustomerAdmin(admin.ModelAdmin):
    list_display = (
        'id',
        'name',
        'attention',
        'email',
        'address',
        'mailing_address',
        'num_members',
    )
    inlines = (
        OrganizationCustomerAttributeInline,
    )

    @mark_safe
    def num_members(self, obj):
        value = '<a href="%s">%s Members</a>' % (
            obj.members_changelist_url,
            obj.members.count(),
        )
        return value
    num_members.allow_tags = True
    num_members.short_description = 'No. of Members'
