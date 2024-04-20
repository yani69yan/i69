# Generated by Django 3.1.5 on 2022-10-14 19:02

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ("user", "0011_user_user_last_seen"),
    ]

    operations = [
        migrations.CreateModel(
            name="ChatsQue",
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
                ("room_id", models.IntegerField()),
                ("isAssigned", models.BooleanField(default=False)),
                ("updated_at", models.DateTimeField(auto_now=True, null=True)),
                ("date_created", models.DateTimeField(auto_now_add=True)),
                (
                    "moderator",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="chat_fake_user",
                        to=settings.AUTH_USER_MODEL,
                    ),
                ),
                (
                    "worker",
                    models.ForeignKey(
                        null=True,
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="chat_active_worker",
                        to=settings.AUTH_USER_MODEL,
                    ),
                ),
            ],
        ),
    ]