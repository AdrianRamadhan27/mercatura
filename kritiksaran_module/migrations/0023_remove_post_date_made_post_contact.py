# Generated by Django 4.1 on 2022-10-31 14:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("kritiksaran_module", "0022_delete_like"),
    ]

    operations = [
        migrations.RemoveField(model_name="post", name="date_made",),
        migrations.AddField(
            model_name="post",
            name="contact",
            field=models.IntegerField(default=0),
            preserve_default=False,
        ),
    ]
