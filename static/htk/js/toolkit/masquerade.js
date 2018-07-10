//
var debugHandle = $('.htk-debug-toolbar-handle');
var debugToolbar = $('.htk-debug-toolbar');
var debugToolbarHideButton = $('.htk-debug-toolbar-hide');

// User ID elements
var masqueradeUserIDForm = $('.masquerade-form-user-id');
var masqueradeUserIDInput = $('.masquerade-form-user-id .masquerade-input');
var masqueradeUserIDButton = $('.masquerade-form-user-id .masquerade-button');
var masqueradeUserIDStopButton = $('.masquerade-user-id-stop');
var masqueradeUserIDTitle = $('.masquerade-user-id-title');
var EMULATE_USER_ID = 'emulate_user_id';

// Username elements
var masqueradeUsernameForm = $('.masquerade-form-username');
var masqueradeUsernameInput = $('.masquerade-form-username .masquerade-input');
var masqueradeUsernameButton = $('.masquerade-form-username .masquerade-button');
var masqueradeUsernameStopButton = $('.masquerade-username-stop');
var masqueradeUsernameTitle = $('.masquerade-username-title');
var EMULATE_USERNAME = 'emulate_user_username';

debugHandle.click(function () {
    debugToolbar.show();
    debugHandle.hide();
});

debugToolbarHideButton.click(function () {
    debugToolbar.hide();
    debugHandle.show();
});

masqueradeUserIDButton.click(function () {
    var cookieVal = masqueradeUserIDInput.val();
    $.cookie(EMULATE_USER_ID, cookieVal);
    location.reload();
});

masqueradeUsernameButton.click(function () {
    var cookieVal = masqueradeUsernameInput.val();
    $.cookie(EMULATE_USERNAME, cookieVal);
    location.reload();
});

masqueradeUserIDStopButton.click(function () {
    $.removeCookie(EMULATE_USER_ID, null);
    location.reload();
})

masqueradeUsernameStopButton.click(function () {
    $.removeCookie(EMULATE_USERNAME, null);
    location.reload();
})

if ($.cookie(EMULATE_USER_ID)) {
    masqueradeUserIDStopButton.show();
    masqueradeUserIDForm.hide();

    masqueradeUsernameForm.hide();
    masqueradeUsernameStopButton.hide();
    masqueradeUsernameTitle.hide();
} else if ($.cookie(EMULATE_USERNAME)) {
    masqueradeUsernameStopButton.show();
    masqueradeUsernameForm.hide();

    masqueradeUserIDForm.hide();
    masqueradeUserIDStopButton.hide();
    masqueradeUserIDTitle.hide();
} else {
    masqueradeUserIDForm.show();
    masqueradeUserIDStopButton.hide();
    masqueradeUserIDTitle.show();

    masqueradeUsernameForm.show();
    masqueradeUsernameStopButton.hide(); masqueradeUsernameTitle.show();
}