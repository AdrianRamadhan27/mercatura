# Generated by Django 4.1 on 2022-10-27 08:06

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('artikel', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='post',
            old_name='image',
            new_name='image_url',
        ),
        migrations.RemoveField(
            model_name='post',
            name='like_count',
        ),
    ]
