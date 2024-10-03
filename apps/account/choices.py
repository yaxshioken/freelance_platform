from django.db.models import TextChoices


class AccountRole(TextChoices):
    EMPLOYEE = ("employee", "EMPLOYEE")
    CUSTOMER = ("customer", "CUSTOMER")
