# Generated by Django 3.1.5 on 2023-12-26 19:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0090_auto_20231212_1838'),
    ]

    operations = [
        migrations.AlterField(
            model_name='chatsquesetting',
            name='taskName',
            field=models.CharField(choices=[('inactive_worker_logout_intervel', 'inactive_worker_logout_intervel'), ('inactive_admin_logout_intervel', 'inactive_admin_logout_intervel'), ('unassign_chat_from_inactive_worker_to_active_worker_intervel', 'unassign_chat_from_inactive_worker_to_active_worker_intervel')], max_length=100),
        ),
    ]
