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
