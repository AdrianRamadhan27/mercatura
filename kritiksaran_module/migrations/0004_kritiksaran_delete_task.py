# Generated by Django 4.1 on 2022-10-27 07:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("kritiksaran_module", "0003_task_delete_post"),
    ]

    operations = [
        migrations.CreateModel(
            name="KritikSaran",
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
            ],
        ),
        migrations.DeleteModel(name="Task",),
    ]
