# Generated by Django 4.1 on 2022-10-30 12:19

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ("kritiksaran_module", "0019_rename_likes_post_liked"),
    ]

    operations = [
        migrations.AddField(
            model_name="post",
            name="date_made",
            field=models.DateTimeField(
                auto_now_add=True, default=django.utils.timezone.now
            ),
            preserve_default=False,
        ),
    ]
