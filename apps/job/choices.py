from django.db import models


class JobTypeChoice(models.TextChoices):
    FIXED_PRICE = "fixed_price", "Fixed Price"
    HOURLY = "hourly", "Hourly"


class PriceMeasureChoice(models.TextChoices):
    UZS = "uzs", "UZS"
    USD = "usd", "USD"


class JobLevel(models.TextChoices):
    JUNIOR = "junior", "Junior"
    MIDDLE = "middle", "Middle"
    SENIOR = "senior", "Senior"
    LEAD = "lead", "Lead"
