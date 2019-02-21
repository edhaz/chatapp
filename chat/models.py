import datetime

from django.db import models
from django.utils import timezone


class Chatter(models.Model):
    name = models.CharField(max_length=200)
    date_joined = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name

    def joined_recently(self):
        return self.date_joined >= timezone.now() - datetime.timedelta(days=1)


class Message(models.Model):
    chatter = models.ForeignKey(Chatter, on_delete=models.CASCADE)
    message = models.CharField(max_length=140)
    posted = models.DateTimeField(auto_now_add=True)
    votes = models.IntegerField(default=0)

    def __str__(self):
        return self.message
