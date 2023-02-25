from __future__ import absolute_import, unicode_literals
import os
from celery import Celery
from django.conf import settings
from celery.schedules import crontab
os.environ.setdefault('DJANGO_SETTINGS_MODULE','massmail.settings')

app=Celery('massmail')
app.conf.enable_utc=False
app.conf.update(timezone='Asia/Kolkata')

app.config_from_object(settings, namespace='CELERY')

#Celery beat settings
app.conf.beat_schedule={
    'send-mail-at-birthday': {
        'task':'bdayemail.tasks.sendSimpleMail',
        'schedule':crontab(hour=12,minute=30),
    }
}

app.autodiscover_tasks()

@app.task(bind=True)
def debug_task(self):
    print(f'Request: {self.request!r}')