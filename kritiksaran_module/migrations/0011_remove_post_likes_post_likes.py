# Generated by Django 4.1 on 2022-10-29 14:55

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ("kritiksaran_module", "0010_post_likes"),
    ]

    operations = [
        migrations.RemoveField(model_name="post", name="likes",),
        migrations.AddField(
            model_name="post",
            name="likes",
            field=models.ManyToManyField(
                related_name="likes", to=settings.AUTH_USER_MODEL
            ),
        ),
    ]
