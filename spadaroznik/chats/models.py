from django.utils import timezone
from django.contrib.auth.models import User
from django.db import models


class Chat(models.Model):
    members = models.ManyToManyField(User)

    def get_absolute_url(self):
        return f'{str(self.id)}'


class Message(models.Model):
    chat = models.ForeignKey(Chat, on_delete=models.SET_NULL, null=True)
    author = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    message = models.TextField()
    pub_date = models.DateTimeField(default=timezone.now)
    is_readed = models.BooleanField(default=False)

    class Meta:
        ordering = ['pub_date']

    def __str__(self):
        return self.message
