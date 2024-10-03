import uuid
from socketserver import ForkingMixIn

from django.core import validators
from django.db import models

from apps.job.choices import JobLevel, JobTypeChoice, PriceMeasureChoice
from apps.shared.models import TimeStampedModel


class JobAnnounce(TimeStampedModel):
    id = models.UUIDField(primary_key=True, unique=True, default=uuid.uuid4)
    title = models.CharField(max_length=255, unique=True)
    body = models.TextField()
    job_type = models.CharField(
        choices=JobTypeChoice.choices, default=JobTypeChoice.FIXED_PRICE
    )
    price = models.DecimalField(decimal_places=2, max_digits=15)
    price_measure = models.CharField(
        choices=PriceMeasureChoice.choices, default=PriceMeasureChoice.USD
    )
    level = models.CharField(choices=JobLevel.choices)
    payment_verified = models.BooleanField(default=False)
    technology = models.ManyToManyField(
        to="technology.Technology", through="job.JobTechnology"
    )
    owner = models.ForeignKey(
        to="account.Account", on_delete=models.CASCADE, related_name="jobs"
    )
    profession = models.ForeignKey(
        to="technology.Profession",
        on_delete=models.CASCADE,
        related_name="jobs",
        null=True,
    )
    location = models.ForeignKey(
        to="job.JobLocation", on_delete=models.CASCADE, related_name="jobs", null=True
    )

    def __str__(self):
        return self.title


class JobTechnology(models.Model):
    job = models.ForeignKey(
        "job.JobAnnounce",
        models.CASCADE,
    )
    technology = models.ForeignKey(
        "technology.Technology",
        models.CASCADE,
    )
    level = models.IntegerField(
        validators=(validators.MaxValueValidator(10), validators.MinValueValidator(1))
    )

    def __str__(self):
        return f"{self.technology} {self.level}"


class JobLocation(TimeStampedModel):
    country = models.CharField(max_length=255)
    city = models.CharField(max_length=255)
