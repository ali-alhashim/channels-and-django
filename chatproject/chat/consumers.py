from channels.generic.websocket import WebsocketConsumer
from asgiref.sync import async_to_sync
import json
from .models import MessageChat, UserChannel
from django.contrib.auth.models import User
from django.utils import timezone
class ChatConsumer(WebsocketConsumer):
    def  connect(self):
        self.accept()
        print("WebsocketConsumer -> connect")
        self.send('{"type":"accept", "status":"accepted"}')
        #print(self.channel_name)
        #async_to_sync(self.channel_layer.group_add)("chat_group", self.channel_name)

        try:
            user_channel = UserChannel.objects.get(user=self.scope.get("user"))
            user_channel.channel_name = self.channel_name
            user_channel.save()
        except:
            user_channel = UserChannel()
            user_channel.user = self.scope.get("user")
            user_channel.channel_name = self.channel_name
            user_channel.save()
       

    def disconnect(self, close_code):
        # Handle WebSocket disconnection here if needed
        print("WebsocketConsumer -> disconnect -> close_code:", close_code)

    def receive(self, text_data):
        text_data = json.loads(text_data)
        #self.send('{"type":"event_arrive", "status":"arrive"}')
        print(text_data.get("type"))
        print(text_data.get("message"))
        new_message = MessageChat()
        new_message.from_who = self.scope.get("user")
        new_message.to_who  = User.objects.get(username = text_data.get("to_who"))
        new_message.message = text_data.get("message")
        new_message.date = timezone.now()
        new_message.time = timezone.now()
        new_message.has_been_seen = False
        new_message.save()

        try:
            the_channel_name = UserChannel.objects.get(user__username = text_data.get("to_who"))
            data = {"type":"recevier_function",
                    "type_of_data":"new_message",
                    "from_who":self.scope.get("user").username,
                    "data":text_data.get("message")
                    }
            async_to_sync(self.channel_layer.send)(the_channel_name.channel_name, data)
        except Exception as e:
            print(e)

    def recevier_function(self, the_data_layer):
        print("the_data_layer -> ", the_data_layer)
        data = json.dumps(the_data_layer)
        self.send(data)