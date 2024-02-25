import json
from channels.generic.websocket import AsyncWebsocketConsumer
from asgiref.sync import sync_to_async
from django.contrib.auth.models import User
from .models import Box, Messages
####
class ChatConsumer(AsyncWebsocketConsumer):
    async def connect(self):
        self.chatbox_name = self.scope['url_route']['kwargs']['chatbox_name']
        self.chatbox_group_name = 'chat_%s' % self.chatbox_name

        await self.channel_layer.group_add(
            self.chatbox_group_name,
            self.channel_name
        )

        await self.accept()
    
    async def disconnect(self):
        await self.channel_layer.group_discard(
            self.chatbox_group_name,
            self.channel_name
        )

    async def receive(self, text_data):
        data = json.loads(text_data)
        message = data['message']
        username = data['username']
        chatbox = data['chatbox']

        await self.save_message(username, chatbox, message)

        await self.channel_layer.group_send(
            self.chatbox_group_name,
            {
                'type':'chat_message',
                'message':message,
                'username':username,
                'chatbox':chatbox,
            }
        )
    
    async def chat_message(self, event):
        message = event['message']
        username = event['username']
        chatbox = event['chatbox']

        await self.send(text_data=json.dumps({
            'message':message,
            'username':username,
            'chatbox':chatbox,
        }))

    @sync_to_async
    def save_message(self, username, chatbox, message):
        user = User.objects.get(username=username)
        chatbox = Box.objects.get(slug=chatbox)

        Messages.objects.create(user=user, chatbox=chatbox, content=message)

