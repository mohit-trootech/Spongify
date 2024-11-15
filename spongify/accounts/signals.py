# Accounts App Signals

from django.db.models.signals import post_save
from django.dispatch import receiver
from utils.base_utils import get_model
from accounts.tasks import customer_registration_mail
from accounts.constants import Choices

User = get_model(app_name="accounts", model_name="User")


@receiver(post_save, sender=User)
def send_mail_after_user_creation(sender, instance, created, **kwargs):
    if created and instance.account_type == Choices.CUSTOMER:
        customer_registration_mail.delay(
            user=instance.username.title(), email=instance.email
        )
