# Generated by Django 3.1.5 on 2022-12-08 15:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("purchase", "0003_package_packagepurchase"),
    ]

    operations = [
        migrations.AddField(
            model_name="purchase",
            name="payment_method",
            field=models.CharField(blank=True, default=None, max_length=255, null=True),
        ),
    ]
