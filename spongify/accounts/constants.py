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

    # Otp Classes
    OTP_CLASS = "w-14 h-14 text-center text-2xl font-extrabold text-slate-900 bg-slate-100 border border-slate-900 hover:border-slate-200 appearance-none rounded p-4 outline-none focus:bg-white focus:border-indigo-400 focus:ring-2 focus:ring-indigo-100 focus:ring-opacity"


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


class AuthErrors:
    """Auth Accounts Error"""

    INVALID_USERNAME_PASSWORD = "Invalid username or password"
    PASSWORD_MISMATCH = "Passwords do not match"
    INVALID_OTP = "Invalid OTP"
    EMAIL_NOT_FOUND = "Email does not exist"
    SESSION_EXPIRED = "Session Expired!"
    OTP_EXPIRED = "OTP Expired!"


class AuthMessages:
    """Auth Accounts Messages"""

    REGISTER_SUCCESS = "Registered successfully"
    LOGIN_SUCCESS = "Login successfully"
    LOGOUT_SUCCESS = "Logged out successfully"
    PASSWORD_RESET_OTP_SENT = "Password reset otp sent to your email"
    OTP_VERIFIED_SUCCESSFULLY = "OTP verified successfully"


class Templates:
    """Accounts app templates paths"""

    PASSWORD_RESET = "accounts/password_reset.html"
    PASSWORD_RESET_DONE = "accounts/password_reset_done.html"
    LOGIN = "accounts/login.html"
    REGISTER = "accounts/register.html"


class UrlPaths:
    """Accounts app url paths"""

    HOME = "/"
    PASSWORD_RESET = "/accounts/password-reset/"
    PASSWORD_RESET_DONE = "/accounts/password-reset-done/"
    LOGIN = "/accounts/login/"
    REGISTER = "/accounts/register/"
