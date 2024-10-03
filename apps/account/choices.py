from django.db.models import TextChoices


class AccountRole(TextChoices):
    EMPLOYEE = ("employee", "EMPLOYEE")
    CUSTOMER = ("customer", "CUSTOMER")


class NotificationTypeChoice(TextChoices):
    JOB_ANNOUNCE = "job_announce", "Job Announce"
    JOB_CONTRACT = "job_contract", "Job Contract"
    CHAT_MESSAGE = "chat_message", "Chat Message"
    OTHER = "other", "Other"
