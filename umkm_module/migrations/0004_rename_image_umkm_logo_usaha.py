# Generated by Django 4.1 on 2022-10-28 16:47

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('umkm_module', '0003_rename_kontak_usaha_umkm_email_usaha_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='umkm',
            old_name='image',
            new_name='logo_usaha',
        ),
    ]
