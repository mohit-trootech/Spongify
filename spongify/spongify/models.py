# Spongify Models

from django.db import models
from spongify.constants import VerboseNames, EmailTemplatesChoice


class EmailTemplate(models.Model):
    """Email Templates"""

    subject = models.CharField(verbose_name=VerboseNames.SUBJECT, max_length=255)
    body = models.TextField(
        verbose_name=VerboseNames.BODY,
    )
    choice = models.CharField(
        verbose_name=VerboseNames.CHOICE,
        choices=EmailTemplatesChoice.TEMPLATE_CHOICES,
        max_length=255,
        unique=True,
    )
    template = models.TextField(
        verbose_name=VerboseNames.TEMPLATE,
    )
    is_html = models.BooleanField(default=True)

    def __str__(self):
        return self.choice

    class Meta:
        verbose_name = VerboseNames.EMAIL_TEMPLATE
        verbose_name_plural = VerboseNames.EMAIL_TEMPLATES


class CreatorWaitlist(models.Model):
    """Creator Waitlist"""

    user = models.ForeignKey(
        "accounts.User", on_delete=models.CASCADE, related_name="creator_waitlist"
    )

    def __str__(self):
        return self.user.username
