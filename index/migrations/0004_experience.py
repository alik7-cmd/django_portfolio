# Generated by Django 4.2.2 on 2023-06-19 17:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("index", "0003_education"),
    ]

    operations = [
        migrations.CreateModel(
            name="Experience",
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
                ("company_name", models.CharField(max_length=30)),
                ("position", models.CharField(max_length=30)),
                ("start_year", models.CharField(max_length=30)),
                ("end_year", models.CharField(max_length=30)),
                ("job_responsibility", models.CharField(max_length=1000)),
            ],
        ),
    ]
