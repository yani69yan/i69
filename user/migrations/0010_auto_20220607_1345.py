# Generated by Django 3.1.5 on 2022-06-07 13:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("user", "0009_moderatorque"),
    ]

    operations = [
        migrations.AlterField(
            model_name="moderatorque",
            name="isAssigned",
            field=models.BooleanField(default=False),
        ),
    ]
