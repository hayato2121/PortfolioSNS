# Generated by Django 4.1.7 on 2023-03-16 13:24

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ("snsapp", "0008_alter_comment_options_comment_like"),
    ]

    operations = [
        migrations.AlterField(
            model_name="comment",
            name="like",
            field=models.ManyToManyField(
                blank=True, related_name="related_commnet", to=settings.AUTH_USER_MODEL
            ),
        ),
    ]