# Generated by Django 5.1 on 2024-11-25 05:58

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):
    replaces = [("spongify", "0001_initial"), ("spongify", "0002_creatorwishlist")]

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name="EmailTemplate",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("subject", models.CharField(max_length=255, verbose_name="Subject")),
                ("body", models.TextField(verbose_name="Body")),
                (
                    "choice",
                    models.CharField(
                        choices=[
                            ("registration", "Registration"),
                            ("account_confirm", "Account Confirm"),
                            ("account_confirm_done", "Account Confirm Done"),
                            ("reset_password", "Reset Password"),
                            ("reset_password_done", "Reset Password Done"),
                            ("change_password", "Change Password"),
                            (
                                "artist_registration_request",
                                "Artist Registration Request",
                            ),
                            (
                                "artist_registration_approval",
                                "Artist Registration Approval",
                            ),
                            (
                                "artist_registration_rejection",
                                "Artist Registration Rejection",
                            ),
                        ],
                        max_length=255,
                        unique=True,
                        verbose_name="Choice",
                    ),
                ),
                ("template", models.TextField(verbose_name="Email Template")),
                ("is_html", models.BooleanField(default=True)),
            ],
            options={
                "verbose_name": "Email Template",
                "verbose_name_plural": "Email Templates",
            },
        ),
        migrations.CreateModel(
            name="CreatorWaitlist",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                (
                    "user",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="creator_waitlist",
                        to=settings.AUTH_USER_MODEL,
                    ),
                ),
            ],
        ),
        migrations.CreateModel(
            name="CreatorWaitlist",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                (
                    "user",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="creator_waitlist",
                        to=settings.AUTH_USER_MODEL,
                    ),
                ),
            ],
        ),
    ]
