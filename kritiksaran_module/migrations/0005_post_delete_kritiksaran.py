# Generated by Django 4.1 on 2022-10-27 16:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("kritiksaran_module", "0004_kritiksaran_delete_task"),
    ]

    operations = [
        migrations.CreateModel(
            name="Post",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("title", models.CharField(max_length=50)),
                ("description", models.TextField()),
            ],
        ),
        migrations.DeleteModel(name="KritikSaran",),
    ]
