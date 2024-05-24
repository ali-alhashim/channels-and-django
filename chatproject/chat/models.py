from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class MessageChat(models.Model):
    from_who      = models.ForeignKey(User, on_delete=models.CASCADE, related_name='messages_from')
    to_who        = models.ForeignKey(User, on_delete=models.CASCADE, related_name='messages_to')
    message       = models.TextField()
    date          = models.DateField(null=True)
    time          = models.TimeField(null=True)
    has_been_seen = models.BooleanField(default=False)
    



class UserChannel(models.Model):
    user         = models.ForeignKey(User, on_delete=models.CASCADE, related_name='user_channels')
    channel_name = models.CharField(max_length=255)