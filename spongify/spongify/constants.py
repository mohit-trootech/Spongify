# Spongify App Constants
from django.utils.translation import gettext_noop as _


class VerboseNames:
    """Spongify App Verbose Names"""

    # Email Template Model
    EMAIL_TEMPLATE = "Email Template"
    EMAIL_TEMPLATES = "Email Templates"
    SUBJECT = "Subject"
    BODY = "Body"
    TEMPLATE = "Email Template"
    CHOICE = "Choice"
    IS_HTML = "Is HTML"


class EmailTemplatesChoice:
    """Email Templates Choice"""

    REGISTRATION = "registration"
    ACCOUNT_CONFIRM = "account_confirm"
    ACCOUNT_CONFIRM_DONE = "account_confirm_done"
    RESET_PASSWORD = "reset_password"
    RESET_PASSWORD_DONE = "reset_password_done"
    CHANGE_PASSWORD_DONE = "change_password"
    ARTIST_REGISTRATION_REQUEST = "artist_registration_request"
    ARTIST_REGISTRATION_APPROVAL = "artist_registration_approval"
    ARTIST_REGISTRATION_REJECTION = "artist_registration_rejection"

    # Choices Tuple
    TEMPLATE_CHOICES = (
        (REGISTRATION, _("Registration")),
        (ACCOUNT_CONFIRM, _("Account Confirm")),
        (ACCOUNT_CONFIRM_DONE, _("Account Confirm Done")),
        (RESET_PASSWORD, _("Reset Password")),
        (RESET_PASSWORD_DONE, _("Reset Password Done")),
        (CHANGE_PASSWORD_DONE, _("Change Password")),
        (ARTIST_REGISTRATION_REQUEST, _("Artist Registration Request")),
        (ARTIST_REGISTRATION_APPROVAL, _("Artist Registration Approval")),
        (ARTIST_REGISTRATION_REJECTION, _("Artist Registration Rejection")),
    )


class Templates:
    """Spongify Template Names"""

    INDEX = "index.html"
    CREATOR_TEMPLATE = "creator/creator.html"


class Reverse:
    """Urls Reverse"""

    HOME = "home"
    CREATOR = "creator"
    CREATOR_JOIN = "creator-join"


class AuthErrors:
    """Music Authentication Errors"""

    NOT_REGISTERED = "User is not authenticated, Login to continue."
    ARTIST_NOT_FOUND = "Artist Not Found!"
    USER_NOT_FOUND = "User Not Found!"


class AuthMessages:
    """Music Authentication Messages"""

    CREATOR_REGISTRATION_JOINED = (
        "You successfully joined the waitlist, Check email for updates."
    )
    ALREADY_JOINED = _("You have already joined the waitlist. Wait for approval.")
    VERIFIED_ARTIST = _("You are a verified artist, Welcome {user}!")


class UrlPaths:
    """Music Url Paths"""

    HOME = "/"
    CREATOR = "/creator/"
    CREATOR_JOIN = "/creator/join/"
