import json

from channels.db import database_sync_to_async
from channels.generic.websocket import AsyncWebsocketConsumer
from .models import Message


class ChatConsumer(AsyncWebsocketConsumer):    
    # Bağlantı başladığında
    async def connect(self):
        self.room_name = self.scope["url_route"]["kwargs"]["room_name"]
        self.room_group_name = f"chat_{self.room_name}"
        print("baglandi")
        # Join room group
        await self.channel_layer.group_add(
            self.room_group_name, self.channel_name
        )

        await self.accept()

    async def disconnect(self, close_code):
        # Leave room group
        await self.channel_layer.group_discard(
            self.room_group_name, self.channel_name
        )

    # Receive message from WebSocket // istemciden mesaj geldinde
    async def receive(self, text_data):
        text_data_json = json.loads(text_data)
        message = text_data_json["message"]
        what_is_it = text_data_json["what_is_it"] 
        user=self.scope["user"]
        
        # print(message) #?test noktasi
        
        await self.save_to_database(message,user,self.room_name,what_is_it)
        
        # Send message to room group
        await self.channel_layer.group_send(
            self.room_group_name, 
            {
                "type": "chat.message",
                "message": message,
                "user": user.username,
                "created_date": self.message_object.get_short_date(),
                "what_is_it":  what_is_it,
            }
        )

    # Receive message from room group // websocketden sohbet kapatıldı
    async def chat_message(self, event):
        message = event["message"]
        user=event["user"]
        created_date=event["created_date"]
        what_is_it=event["what_is_it"]
        # Send message to WebSocket
        await self.send(text_data=json.dumps(
            {
                "message": message,
                "user": user,
                "created_date": created_date,
                "what_is_it": what_is_it,
            }))
        
    
    @database_sync_to_async
    def save_to_database(self,message,user,room,what_is_it):
        m=Message.objects.create(content=message,user=user,room_id=room,what_is_it=what_is_it)
        self.message_object=m