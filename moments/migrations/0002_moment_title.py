# Generated by Django 3.1.5 on 2022-01-22 05:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("moments", "0001_initial"),
    ]

    operations = [
        migrations.AddField(
            model_name="moment",
            name="Title",
            field=models.CharField(max_length=100, null=True),
        ),
    ]