from django.contrib.auth.models import AbstractUser
from django.db import models
from phonenumber_field.modelfields import PhoneNumberField

from apps.account.choices import AccountRole
from apps.shared.models import TimeStampedModel


class Account(AbstractUser, TimeStampedModel):
    phone = PhoneNumberField(unique=True)
    is_active = models.BooleanField(default=False)
    role = models.CharField(
        max_length=255, choices=AccountRole.choices, default=AccountRole.EMPLOYEE
    )
    USERNAME_FIELD = "phone"

    def __str__(self):
        return self.phone.as_e164


class AccountInfo(TimeStampedModel):
    bio = models.CharField(max_length=255, null=True, blank=True)
    profession = models.ForeignKey(
        "technology.Profession", on_delete=models.SET_NULL, null=True
    )
    technologies = models.ForeignKey(
        "technology.Technology", on_delete=models.SET_NULL, null=True
    )
    is_visible = models.BooleanField(default=False)
    account = models.OneToOneField(Account, on_delete=models.CASCADE)

    def __str__(self):
        return self.profession.name if self.profession else "No Profession"
