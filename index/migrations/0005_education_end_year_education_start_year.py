# Generated by Django 4.2.2 on 2023-06-20 08:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("index", "0004_experience"),
    ]

    operations = [
        migrations.AddField(
            model_name="education",
            name="end_year",
            field=models.CharField(default="", max_length=10),
        ),
        migrations.AddField(
            model_name="education",
            name="start_year",
            field=models.CharField(default="", max_length=10),
        ),
    ]