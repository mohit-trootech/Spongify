from django.db import models
from django.contrib.auth.models import AbstractUser
from phonenumber_field.modelfields import PhoneNumberField
from accounts.constants import VerboseNames, Choices
from django_extensions.db.fields import CreationDateTimeField


class User(AbstractUser):
    email = models.EmailField(verbose_name=VerboseNames.EMAIL, unique=True)
    age = models.IntegerField(verbose_name=VerboseNames.AGE, blank=True, null=True)
    phone_number = PhoneNumberField(
        verbose_name=VerboseNames.PHONE_NUMBER, region="IN", blank=True, null=True
    )
    account_verified = models.BooleanField(
        choices=Choices.ACCOUNT_VERIFIED_CHOICE,
        default=Choices.UNVERIFIED,
        verbose_name=VerboseNames.ACCOUNT_VERIFIED,
    )
    gender = models.CharField(
        choices=Choices.GENDER_CHOICE,
        max_length=10,
        verbose_name=VerboseNames.GENDER,
        blank=True,
        null=True,
    )
    account_type = models.CharField(
        default=Choices.CUSTOMER,
        choices=Choices.ACCOUNT_TYPE_CHOICE,
        verbose_name=VerboseNames.ACCOUNT_TYPE,
        max_length=50,
        blank=True,
        null=True,
    )
    created = CreationDateTimeField()

    modified = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.username

    class Meta:
        verbose_name = VerboseNames.USER
        verbose_name_plural = VerboseNames.USERS


class Otp(models.Model):
    user = models.ForeignKey(
        "accounts.User",
        on_delete=models.CASCADE,
        related_name=VerboseNames.OTP_O2O_USER,
    )
    otp = models.CharField(max_length=6)
    created = CreationDateTimeField()
    expiry = models.DateTimeField()

    def __str__(self):
        return VerboseNames.OTP_STR.format(users=self.user.username)

    class Meta:
        verbose_name = VerboseNames.OTP
        verbose_name_plural = VerboseNames.OTPS
