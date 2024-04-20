# Generated by Django 3.1.5 on 2022-11-01 18:37

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ("payments", "0007_auto_20221031_1609"),
    ]

    operations = [
        migrations.CreateModel(
            name="ChargeError",
            fields=[
                (
                    "id",
                    models.AutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("message", models.CharField(max_length=155)),
                (
                    "charge",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="errors",
                        to="payments.charge",
                    ),
                ),
            ],
        ),
    ]
