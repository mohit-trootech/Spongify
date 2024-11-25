from django.db import models
from django.contrib.auth.models import AbstractUser
from phonenumber_field.modelfields import PhoneNumberField
from accounts.constants import VerboseNames, Choices
from django_extensions.db.models import TimeStampedModel
from django_extensions.db.fields import CreationDateTimeField
from django.utils.timezone import now, timedelta
from random import randint


def _generate_otp():
    return randint(100000, 999999)


def _upload_to(self, filename):
    return f"user/{self.username}/{filename}"


class User(AbstractUser, TimeStampedModel):
    image = models.ImageField(upload_to=_upload_to, blank=True, null=True)

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

    def __str__(self):
        return self.username

    class Meta:
        verbose_name = VerboseNames.USER
        verbose_name_plural = VerboseNames.USERS


class Otp(models.Model):
    user = models.OneToOneField(
        "accounts.User",
        on_delete=models.CASCADE,
        related_name=VerboseNames.OTP_O2O_USER,
    )
    otp = models.CharField(max_length=6, default=_generate_otp)
    created = CreationDateTimeField()
    expiry = models.DateTimeField()

    def __str__(self):
        return VerboseNames.OTP_STR.format(users=self.user.username)

    class Meta:
        verbose_name = VerboseNames.OTP
        verbose_name_plural = VerboseNames.OTPS

    def save(self, *args, **kwargs):
        self.expiry = now() + timedelta(minutes=10)
        super().save(*args, **kwargs)

    @property
    def is_expired(self):
        return now() > self.expiry
