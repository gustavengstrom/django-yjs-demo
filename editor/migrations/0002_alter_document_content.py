# Generated by Django 4.2.13 on 2025-03-24 08:33

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("editor", "0001_initial"),
    ]

    operations = [
        migrations.AlterField(
            model_name="document",
            name="content",
            field=models.TextField(default=""),
        ),
    ]
