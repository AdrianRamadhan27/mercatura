# Generated by Django 4.1 on 2022-10-30 09:31

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("kritiksaran_module", "0014_like"),
    ]

    operations = [
        migrations.RemoveField(model_name="post", name="liked",),
        migrations.DeleteModel(name="Like",),
    ]
