# Generated by Django 4.1.7 on 2023-03-20 16:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("accounts", "0004_customuser_bg_image"),
    ]

    operations = [
        migrations.AddField(
            model_name="customuser",
            name="content",
            field=models.TextField(blank=True, null=True, verbose_name="本文"),
        ),
    ]
