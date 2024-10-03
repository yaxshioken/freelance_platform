from config.celery import app


@app.task(bind=True, ignore_result=True)
def create_notification_for_developers(self,):
    pass