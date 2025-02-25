from celery import shared_task
from utils.email_services import EmailService
from utils.base_utils import get_model

User = get_model("accounts", "User")


@shared_task
def artist_signup_mail_task(id: int):
    """
    Send Creator Signup Mail Requested by User

    Parameters
    ----------
    id : int
        User's ID
    """
    return EmailService().artist_signup_mail(User.objects.get(id=id))


@shared_task
def artist_signup_approval_task(id: int):
    """
    Send Creator Signup Approval Mail to User

    Parameters
    ----------
    id : int
        User's ID
    """
    return EmailService().artist_signup_approval_mail(User.objects.get(id=id))


@shared_task
def artist_signup_rejection_task(id: int):
    """
    Send Creator Signup Rejection Mail to User

    Parameters
    ----------
    id : int
        User's ID
    """
    return EmailService().artist_signup_rejection_mail(User.objects.get(id=id))
