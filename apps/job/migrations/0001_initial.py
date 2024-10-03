# Generated by Django 5.1.1 on 2024-10-03 10:08

import uuid

import django.core.validators
import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ("technology", "0001_initial"),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name="JobLocation",
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
                ("created_at", models.DateTimeField(auto_now_add=True)),
                ("updated_at", models.DateTimeField(auto_now=True)),
                ("country", models.CharField(max_length=255)),
                ("city", models.CharField(max_length=255)),
            ],
            options={
                "ordering": ["-created_at"],
                "abstract": False,
            },
        ),
        migrations.CreateModel(
            name="JobAnnounce",
            fields=[
                ("created_at", models.DateTimeField(auto_now_add=True)),
                ("updated_at", models.DateTimeField(auto_now=True)),
                (
                    "id",
                    models.UUIDField(
                        default=uuid.uuid4,
                        primary_key=True,
                        serialize=False,
                        unique=True,
                    ),
                ),
                ("title", models.CharField(max_length=255)),
                ("body", models.TextField()),
                (
                    "job_type",
                    models.CharField(
                        choices=[("fixed_price", "Fixed Price"), ("hourly", "Hourly")],
                        default="fixed_price",
                    ),
                ),
                ("price", models.DecimalField(decimal_places=2, max_digits=15)),
                (
                    "price_measure",
                    models.CharField(
                        choices=[("uzs", "UZS"), ("usd", "USD")], default="usd"
                    ),
                ),
                (
                    "level",
                    models.CharField(
                        choices=[
                            ("junior", "Junior"),
                            ("middle", "Middle"),
                            ("senior", "Senior"),
                            ("lead", "Lead"),
                        ]
                    ),
                ),
                ("payment_verified", models.BooleanField(default=False)),
                (
                    "owner",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="jobs",
                        to=settings.AUTH_USER_MODEL,
                    ),
                ),
                (
                    "profession",
                    models.ForeignKey(
                        null=True,
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="jobs",
                        to="technology.profession",
                    ),
                ),
                (
                    "location",
                    models.ForeignKey(
                        null=True,
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="jobs",
                        to="job.joblocation",
                    ),
                ),
            ],
            options={
                "ordering": ["-created_at"],
                "abstract": False,
            },
        ),
        migrations.CreateModel(
            name="JobTechnology",
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
                    "level",
                    models.IntegerField(
                        validators=[
                            django.core.validators.MaxValueValidator(10),
                            django.core.validators.MinValueValidator(1),
                        ]
                    ),
                ),
                (
                    "job",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="job.jobannounce",
                    ),
                ),
                (
                    "technology",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="technology.technology",
                    ),
                ),
            ],
        ),
        migrations.AddField(
            model_name="jobannounce",
            name="technology",
            field=models.ManyToManyField(
                through="job.JobTechnology", to="technology.technology"
            ),
        ),
    ]