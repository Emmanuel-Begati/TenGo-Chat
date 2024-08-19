from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class ChatGroup(models.Model):
    group_name = models.CharField(max_length=128, unique=True)
    # description = models.TextField()
    # members = models.ManyToManyField('a_users.CustomUser', related_name='chat_groups')
    # date_created = models.DateTimeField(auto_now_add=True)
    # date_updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.group_name
    

class ChatGroupMessage(models.Model):
    group = models.ForeignKey(ChatGroup, on_delete=models.CASCADE, related_name='messages')
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    body = models.TextField(max_length=1024)
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.body