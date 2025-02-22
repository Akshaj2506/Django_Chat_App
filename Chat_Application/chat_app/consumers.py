import json
from channels.generic.websocket import AsyncWebsocketConsumer
from django.contrib.auth.models import User
from asgiref.sync import sync_to_async
from .models import ChatMessage

class ChatConsumer(AsyncWebsocketConsumer):
   async def connect(self):
        self.user = self.scope['user']
        self.other_user_id = self.scope['url_route']['kwargs']['user_id']
        self.room_group_name = f"chat_{min(self.user.id, int(self.other_user_id))}_{max(self.user.id, int(self.other_user_id))}"

        await self.channel_layer.group_add(
            self.room_group_name,
            self.channel_name
        )
        await self.accept()

   async def disconnect(self, close_code):
      await self.channel_layer.group_discard(
         self.room_group_name,
         self.channel_name
      )

   async def receive(self, text_data):
      data = json.loads(text_data)
      message = data['message']
      sender = self.user
      receiver = await sync_to_async(User.objects.get)(id=self.other_user_id)

      await sync_to_async(ChatMessage.objects.create)(
         sender=sender, receiver=receiver, message=message
      )


      await self.channel_layer.group_send(
         self.room_group_name,
         {
               'type': 'chat_message',
               'message': message,
               'sender': sender.username
         }
   )

   async def chat_message(self, event):
        message = event['message']
        sender = event['sender']

        await self.send(text_data=json.dumps({
            'message': message,
            'sender': sender
        }))