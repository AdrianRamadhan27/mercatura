# Generated by Django 4.1 on 2022-10-30 10:02

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("kritiksaran_module", "0018_rename_liked_post_likes"),
    ]

    operations = [
        migrations.RenameField(model_name="post", old_name="likes", new_name="liked",),
    ]
