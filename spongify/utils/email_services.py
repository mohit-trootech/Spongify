# Email Service
from django.core.mail import EmailMultiAlternatives
from django.conf import settings
from utils.base_utils import get_model
from spongify.models import EmailTemplatesChoice

EmailTemplate = get_model(app_name="spongify", model_name="EmailTemplate")


class EmailService:
    """Email Service Class"""

    @staticmethod
    def send_email(
        subject: str,
        body: str,
        to_email: list,
        template: str,
        is_html: bool = False,
    ):
        """
        Email Service - default static method to send mail

        Parameters
        ----------
        subject : str
            Email Description
        body : str
            Email Text Body
        to_email : str
            List of receipients
        template : str
            HTML template
        is_html : bool, optional
            Is HTML email template, by default False
        """
        sender = settings.EMAIL_HOST_USER
        msg = EmailMultiAlternatives(
            subject=subject, from_email=sender, to=to_email, body=body
        )
        if is_html:
            msg.attach_alternative(template, "text/html")
        msg.send(fail_silently=False)
        return "Email Sent Successfully"

    @staticmethod
    def get_email_template(choice: str):
        """
        returns email template from template choice provided

        Parameters
        ----------
        choice : str
            Email templates choice
        """
        try:
            return EmailTemplate.objects.get(choice=choice)
        except EmailTemplate.DoesNotExist:
            return None

    def send_registration_mail(self, user: str, email: str):
        """Send Registeration Mail to User"""
        template = self.get_email_template(choice=EmailTemplatesChoice.REGISTRATION)
        if not template:
            return "Email Template Not Found"
        return self.send_email(
            subject=template.subject.format(user=user),
            body=template.body.format(user=user),
            to_email=[email],
            template=template.template.format(user=user),
            is_html=template.is_html,
        )
