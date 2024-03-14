from django.db import models

# Create your models here.

SMS ='SMS'
EMAIL ="EMAIL"
OTHERS = 'Other'

REMINDER_CHOISES = [
    (SMS, 'SMS'),
    (EMAIL,'EMAIL'),
    (OTHERS,'Other'),
]


class Reminders(models.Model):
    date = models.DateField()
    time = models.TimeField()
    message = models.TextField()
    reminder_type =models.CharField(max_length=50 , choices=REMINDER_CHOISES)