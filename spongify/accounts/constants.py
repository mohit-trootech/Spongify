# Accounts App Constants
from django.utils.translation import gettext_noop as _


class VerboseNames:
    """Accounts App Verbose Names"""

    # User Model
    USER = "User"
    USERS = "Users"
    AGE = "Age"
    PHONE_NUMBER = "Phone Number"
    EMAIL = "Email"
    ACCOUNT_VERIFIED = "Account Verified"
    GENDER = "Gender"
    ACCOUNT_TYPE = "Account Type"

    # Otp Model
    OTP = "OTP"
    OTPS = "OTPs"
    OTP_O2O_USER = "otp"
    OTP_STR = "{users}'s OTP"


class Choices:
    """Model Choices"""

    # User Model
    VERIFIED = 1
    UNVERIFIED = 0
    ACCOUNT_VERIFIED_CHOICE = (
        (VERIFIED, _("Verified")),
        (UNVERIFIED, _("Unverified")),
    )
    MALE = "male"
    FEMALE = "female"
    GENDER_CHOICE = (
        (MALE, _("Male")),
        (FEMALE, _("Female")),
    )
    ARTIST = "artist"
    CUSTOMER = "customer"
    ACCOUNT_TYPE_CHOICE = (
        (ARTIST, _("Artist")),
        (CUSTOMER, _("Customer")),
    )


class Reverse:

    REGISTER = "register"
    LOGIN = "login"
    LOGOUT = "logout"
    PASSWORD_RESET = "password-reset"
    PASSWORD_RESET_DONE = "password-reset-done"


class FormsClasses:
    """Custom Classes for Forms"""

    INPUT = "input input-primary input-sm input-bordererd w-full"
    PASSWORD_INPUT = (
        "input input-primary input-sm input-bordererd w-full password-toggle"
    )
    INPUT = "input input-primary input-sm input-bordererd w-full"
    TEXT_AREA = "textarea textarea-primary textarea-sm textarea-bordererd w-full"
    TOGGLE = "toggle toggle-primary toggle-sm "
    SELECT = "select select-primary select-sm select-bordererd w-full"


class FormLabels:
    """Accounts Form Label"""

    REGISTER = {
        "username": "Username",
        "first_name": "First Name",
        "email": "Email",
        "age": "Age",
    }
    LOGIN = {
        "username": "Username",
        "password": "Password",
    }
    PASSWORD_RESET = {
        "email": "Email",
    }


class FormPlaceholder:
    """Accounts Forms Placeholder"""

    REGISTER = {
        "username": "Choose username",
        "first_name": "Enter your name",
        "email": "Enter your email",
        "age": "Enter your age",
    }
    LOGIN = {
        "username": "Username",
        "password": "Password",
    }
    PASSWORD_RESET = {
        "email": "Email",
    }


class FormHelpText:
    """Accounts Forms Help Text"""

    REGISTER = {
        "username": "Username must be unique",
        "email": "Email must be unique",
    }
    LOGIN = {
        "username": "Enter your username",
        "password": "Enter your password",
    }
    PASSWORD_RESET = {
        "email": "Enter your email address below and we'll send you a password reset link.",
    }
