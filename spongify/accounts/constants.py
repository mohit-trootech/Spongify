# Accounts App Constants
from django.utils.translation import gettext_noop as _


class VerboseNames:
    """Accounts App Verbose Names"""

    # User Model
    USER = _("User")
    USERS = _("Users")
    AGE = _("Age")
    PHONE_NUMBER = _("Phone Number")
    EMAIL = _("Email")
    ACCOUNT_VERIFIED = _("Account Verified")
    GENDER = _("Gender")
    ACCOUNT_TYPE = _("Account Type")

    # Otp Model
    OTP = _("OTP")
    OTPS = _("OTPs")
    OTP_O2O_USER = _("otp")
    OTP_STR = _("{users}'s OTP")


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
    FORCE_LOGOUT = "force-logout"
    PASSWORD_RESET = "password-reset"
    PASSWORD_RESET_DONE = "password-reset-done"
    PROFILE = "profile"


class FormLabels:
    """Accounts Form Label"""

    REGISTER = {
        "username": _("Username"),
        "first_name": _("First Name"),
        "email": _("Email"),
        "age": _("Age"),
    }
    LOGIN = {
        "username": _("Username"),
        "password": _("Password"),
    }
    PASSWORD_RESET = {
        "email": _("Email"),
    }
    PROFILE = {
        "image": _("Profile Image"),
        "first_name": _("First Name"),
        "last_name": _("Last Name"),
        "email": _("Email"),
        "phone_number": _("Phone Number"),
        "gender": _("Gender"),
        "age": _("Age"),
    }


class FormPlaceholder:
    """Accounts Forms Placeholder"""

    REGISTER = {
        "username": _("Choose username"),
        "first_name": _("Enter your name"),
        "email": _("Enter your email"),
        "age": _("Enter your age"),
    }
    LOGIN = {
        "username": _("Username"),
        "password": _("Password"),
    }
    PASSWORD_RESET = {
        "email": _("Email"),
    }
    PROFILE = {
        "image": _("Choose your Profile image"),
        "first_name": _("Enter your first name"),
        "last_name": _("Enter your last name"),
        "email": _("Enter your email"),
        "phone_number": _("Enter your phone number"),
        "gender": _("Select your gender"),
        "age": _("Enter your age"),
    }


class FormHelpText:
    """Accounts Forms Help Text"""

    REGISTER = {
        "username": _("Username must be unique"),
        "email": _("Email must be unique"),
    }
    LOGIN = {
        "username": _("Enter your username"),
        "password": _("Enter your password"),
    }
    PASSWORD_RESET = {
        "email": _(
            "Enter your email address below and we'll send you a password reset link."
        ),
    }
    PROFILE = {
        "image": _("Choose your Profile image"),
        "email": _("Please choose a valid email, this is used as your primary email"),
        "phone_number": _("Please enter your phone number in format: +91-XXXXXXXXXX"),
    }


class AuthErrors:
    """Auth Accounts Error"""

    INVALID_USERNAME_PASSWORD = _("Invalid username or password")
    PASSWORD_MISMATCH = _("Passwords do not match")
    INVALID_OTP = _("Invalid OTP")
    EMAIL_NOT_FOUND = _("Email does not exist")
    SESSION_EXPIRED = _("Session Expired!")
    OTP_EXPIRED = _("OTP Expired!")


class AuthMessages:
    """Auth Accounts Messages"""

    REGISTER_SUCCESS = _("Registered successfully")
    LOGIN_SUCCESS = _("Login successfully")
    LOGOUT_SUCCESS = _("Logged out successfully")
    PASSWORD_RESET_OTP_SENT = _("Password reset otp sent to your email")
    OTP_VERIFIED_SUCCESSFULLY = _("OTP verified successfully")


class Templates:
    """Accounts app templates paths"""

    PASSWORD_RESET = "accounts/password_reset.html"
    PASSWORD_RESET_DONE = "accounts/password_reset_done.html"
    LOGIN = "accounts/login.html"
    REGISTER = "accounts/register.html"
    PROFILE = "accounts/profile.html"


class UrlPaths:
    """Accounts app url paths"""

    HOME = "/"
    PASSWORD_RESET = "/accounts/password-reset/"
    PASSWORD_RESET_DONE = "/accounts/password-reset-done/"
    LOGIN = "/accounts/login/"
    REGISTER = "/accounts/register/"
    PROFILE = "/accounts/profile/{username}"
