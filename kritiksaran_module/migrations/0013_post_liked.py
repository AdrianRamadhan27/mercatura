# Generated by Django 4.1 on 2022-10-29 18:34

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ("kritiksaran_module", "0012_remove_post_likes"),
    ]

    operations = [
        migrations.AddField(
            model_name="post",
            name="liked",
            field=models.ManyToManyField(
                blank=True, related_name="likes", to=settings.AUTH_USER_MODEL
            ),
        ),
    ]