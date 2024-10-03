import random

from celery import shared_task
from django.core.cache import cache
from twilio.rest import Client

from config.celery import app


@app.task(bind=True, ignore_result=True)
def send_activation_code(self, phone):
    code = random.randint(1000, 9999)
    cache.set(phone, code, 240)
    print(code)
    with open("code.txt", "w") as f:
        f.write(str(code))
