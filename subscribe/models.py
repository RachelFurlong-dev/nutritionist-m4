from django.db import models
from django.utils import timezone

from django.db import models

class Subscriber(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField(unique=True, max_length=100)
    date_subscribed = models.DateTimeField('Date created', default=timezone.now)

    def __str__(self):
        return self.email
