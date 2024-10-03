from django.db import models
from django.utils.text import slugify

from apps.shared.models import SlugStampedModel


class Profession(SlugStampedModel):
    name = models.CharField(max_length=255)
    is_verified = models.BooleanField(default=False)

    def __str__(self):
        return self.name

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.name)
        super().save(*args, **kwargs)


class Technology(SlugStampedModel):
    name = models.CharField(max_length=255)
    is_verified = models.BooleanField(default=False)

    def __str__(self):
        return self.name

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.name)
        super().save(*args, **kwargs)
