# Generated by Django 4.2.2 on 2023-06-13 06:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("index", "0001_initial"),
    ]

    operations = [
        migrations.RenameField(
            model_name="about", old_name="full_name", new_name="first_name",
        ),
        migrations.AddField(
            model_name="about",
            name="last_name",
            field=models.CharField(default="", max_length=30),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name="about",
            name="description",
            field=models.TextField(max_length=300),
        ),
    ]
