# Accounts App Signals

from django.db.models.signals import post_save
from django.dispatch import receiver
from utils.base_utils import get_model

User = get_model(app_name="accounts", model_name="User")


@receiver(post_save, sender=User)
def send_mail_after_user_creation(sender, instance, created, **kwargs):
    if created:
        pass
        # customer_registration_mail.delay(id=instance.id)
