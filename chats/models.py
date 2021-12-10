from django.db import models
from django.contrib.auth.models import User

class Chat(models.Model):
    title = models.CharField(max_length=255)
    owner = models.ForeignKey(User, related_name = 'owner',on_delete=models.CASCADE)
    chat_users = models.ManyToManyField(User, related_name = 'chat_users')
    date_created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title

class Message(models.Model):
    chat = models.ForeignKey(Chat, on_delete=models.CASCADE)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    date_posted = models.DateTimeField(auto_now_add=True)
    content = models.TextField()

