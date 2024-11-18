# Accounts Celery Tasks

from celery import shared_task
from utils.base_utils import get_model
from utils.email_services import EmailService

User = get_model(app_name="accounts", model_name="User")


@shared_task
def customer_registration_mail(id: int):
    """
    Registration Mail for Customer


    Parameters
    ----------
    id : int
        user's primary key

    Returns
    -------
    str
       Email Service Response
    """
    return EmailService().send_registration_mail(user=User.objects.get(id=id))


@shared_task
def password_reset_mail(id: int):
    """
    Send Password Reset Mail to User
    Parameters
    ----------
    id : int
        user's primary key

    Returns
    -------
    str
       Email Service Response
    """
    return EmailService().password_reset_mail_otp(user=User.objects.get(id=id))
