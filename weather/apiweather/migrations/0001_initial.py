# Generated by Django 5.1.1 on 2024-10-05 13:13

from django.db import migrations, models


class Migration(migrations.Migration):
    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Description",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                (
                    "weather_description",
                    models.IntegerField(
                        choices=[
                            (0, "Sunny"),
                            (1, "Rain"),
                            (3, "Cloudy"),
                            (4, "Snow"),
                            (5, "Partly Cloudy"),
                            (6, "Mostly Cloudy"),
                        ],
                        default=0,
                    ),
                ),
                ("temperature", models.FloatField()),
                ("created_on", models.DateTimeField(auto_now_add=True)),
            ],
            options={
                "ordering": ["-created_on"],
            },
        ),
    ]
