# Generated by Django 4.1.7 on 2023-03-16 12:52

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ("snsapp", "0007_remove_post_title"),
    ]

    operations = [
        migrations.AlterModelOptions(
            name="comment",
            options={"ordering": ["-created_at"]},
        ),
        migrations.AddField(
            model_name="comment",
            name="like",
            field=models.ManyToManyField(
                blank=True, related_name="related_comment", to=settings.AUTH_USER_MODEL
            ),
        ),
    ]
