# Email Service
from django.core.mail import EmailMultiAlternatives
from django.conf import settings
from utils.base_utils import get_model
from spongify.models import EmailTemplatesChoice

EmailTemplate = get_model(app_name="spongify", model_name="EmailTemplate")
Otp = get_model(app_name="accounts", model_name="Otp")


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
    def _handle_otp(user):
        """Check Whether OTP Already There For User"""
        try:
            Otp.objects.get(user=user).delete()
        except Otp.DoesNotExist:
            pass
        return Otp.objects.create(user=user)

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
            template = EmailTemplate.objects.get(choice=choice)
            return template
        except EmailTemplate.DoesNotExist:
            return None

    def send_registration_mail(self, user):
        """
        Send Registration Mail to User

        Parameters
        ----------
        user :
            user's instance
        """
        template = self.get_email_template(choice=EmailTemplatesChoice.REGISTRATION)
        if not template:
            return "Email Template Not Found"
        return self.send_email(
            subject=template.subject.format(user=user.username),
            body=template.body.format(user=user.username),
            to_email=[user.email],
            template=template.template.format(user=user.username),
            is_html=template.is_html,
        )

    def password_reset_mail_otp(self, user):
        """
        Send Password Reset Mail to User

        Parameters
        ----------
        user :
            user's instance
        """
        template = self.get_email_template(choice=EmailTemplatesChoice.RESET_PASSWORD)
        otp = self._handle_otp(user=user)
        expiry = otp.expiry.strftime("%B %d %Y, %H:%M %p %Z")
        if not template:
            return "Email Template Not Found"
        return self.send_email(
            subject=template.subject,
            body=template.body.format(otp=otp.otp, expiry=expiry),
            to_email=[user.email],
            template=template.template.format(otp=otp.otp, expiry=expiry),
            is_html=template.is_html,
        )

    def password_reset_mail_done(self, user):
        """
        Send Password Reset Confirm Mail to user

        Parameters
        ----------
        user :
            user's instance
        """
        template = self.get_email_template(
            choice=EmailTemplatesChoice.RESET_PASSWORD_DONE
        )
        return self.send_email(
            subject=template.subject,
            body=template.body.format(username=user.username),
            to_email=[user.email],
            template=template.template,
            is_html=template.is_html,
        )
