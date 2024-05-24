from django.contrib import admin
from .models import MessageChat, UserChannel
# Register your models here.

@admin.register(MessageChat)
class MessageChatAdmin(admin.ModelAdmin):
    list_display = ["from_who", "to_who", "message", "date", "time", "has_been_seen"]
    list_filter  = ["from_who", "to_who", "message", "date", "has_been_seen"]
    search_fields = ["from_who", "to_who", "message", "date", "has_been_seen"]



@admin.register(UserChannel)
class UserChannelAdmin(admin.ModelAdmin):
    list_display = ["user", "channel_name"]
