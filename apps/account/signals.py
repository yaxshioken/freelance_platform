from time import time_ns

from django.db.models.signals import post_save
from django.dispatch import receiver

from apps.account.models import Account, AccountInfo


@receiver(post_save, sender=Account)
def my_handler(sender, instance: Account, created, **kwargs):
    if created:
        instance.username = f"user{str(time_ns())[-6:]}"
        instance.save()
        AccountInfo.objects.create(account=instance)
