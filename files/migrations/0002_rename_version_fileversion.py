# Generated by Django 5.0.4 on 2025-03-17 16:24

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("files", "0001_initial"),
    ]

    operations = [
        migrations.RenameModel(
            old_name="Version",
            new_name="FileVersion",
        ),
    ]
