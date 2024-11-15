# Accounts Celery Tasks

from celery import shared_task

from utils.email_services import EmailService


@shared_task
def customer_registration_mail(user: str, email: str):
    """
    Registration Mail for Customer


    Parameters
    ----------
    user : str
        user's username
    email : str
        user's email

    Returns
    -------
    str
       Email Service Response
    """
    return EmailService().send_registration_mail(user=user, email=email)
