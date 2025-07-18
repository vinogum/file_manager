# Generated by Django 5.0.4 on 2025-03-17 18:34

from django.conf import settings
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("files", "0002_rename_version_fileversion"),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.RenameField(
            model_name="file",
            old_name="name",
            new_name="url",
        ),
        migrations.AlterUniqueTogether(
            name="file",
            unique_together={("user", "url")},
        ),
    ]
