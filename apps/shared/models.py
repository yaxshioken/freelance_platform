from django.db.models import DateTimeField, Model, SlugField

from apps.account import models


class TimeStampedModel(Model):
    created_at = DateTimeField(auto_now_add=True)
    updated_at = DateTimeField(auto_now=True)

    class Meta:
        abstract = True
        ordering = ["-created_at"]


class SlugStampedModel(TimeStampedModel):
    slug = SlugField(unique=True)

    class Meta:
        abstract = True
        ordering = ["-created_at"]
