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
        verbose_name = "Email Template"
        verbose_name_plural = "Email Templates"
