# Generated by Django 3.1.5 on 2023-04-29 08:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('notificationsetting', '0004_auto_20230412_2246'),
    ]

    operations = [
        migrations.AlterField(
            model_name='notificationsound',
            name='name',
            field=models.CharField(choices=[('coin_purchase', 'Coin Purchase'), ('package_purchase', 'Package Purchase'), ('gift_purchase', 'Gift Purchase'), ('new_user', 'New User'), ('report_user', 'Report User'), ('report_moment', 'Report Moment'), ('notification', 'Notification'), ('server_error', 'Server Error')], max_length=255, unique=True),
        ),
    ]