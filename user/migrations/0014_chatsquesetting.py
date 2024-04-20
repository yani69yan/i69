# Generated by Django 3.1.5 on 2022-10-15 07:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("user", "0013_auto_20221015_0231"),
    ]

    operations = [
        migrations.CreateModel(
            name="ChatsQueSetting",
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
                (
                    "taskName",
                    models.CharField(
                        choices=[
                            ("moderator_logout_intervel", "moderator_logout_intervel"),
                            (
                                "unassign_chat_from_inactive_worker_to_active_worker_intervel",
                                "unassign_chat_from_inactive_worker_to_active_worker_intervel",
                            ),
                        ],
                        max_length=100,
                    ),
                ),
                ("numberOfPeriods", models.IntegerField()),
                (
                    "intervalPeriod",
                    models.CharField(
                        choices=[
                            (86400, "Days"),
                            (3600, "Hours"),
                            (60, "Minutes"),
                            (1, "Seconds"),
                        ],
                        max_length=100,
                    ),
                ),
            ],
        ),
    ]