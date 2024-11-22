# Generated by Django 5.1 on 2024-11-22 09:35

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("music", "0006_albumpopularity_trackpopularity"),
    ]

    operations = [
        migrations.AlterField(
            model_name="albumpopularity",
            name="artist",
            field=models.OneToOneField(
                on_delete=django.db.models.deletion.CASCADE,
                related_name="popularity",
                to="music.artist",
            ),
        ),
        migrations.AlterField(
            model_name="trackpopularity",
            name="track",
            field=models.OneToOneField(
                on_delete=django.db.models.deletion.CASCADE,
                related_name="popularity",
                to="music.track",
            ),
        ),
    ]
