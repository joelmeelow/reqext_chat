import json
import datetime
import logging
import os
from channels.generic.websocket import AsyncWebsocketConsumer
from channels.db import database_sync_to_async
from cryptography.fernet import Fernet
from .models import ChatMessage
from home.models import pharmauser, User
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

logger = logging.getLogger(__name__)

class ChatRoomConsumer(AsyncWebsocketConsumer):
    async def connect(self):
        self.group_name = self.scope['url_route']['kwargs']['group_name']
        self.user = self.scope["user"]
        self.room_group_name = self.group_name
        await self.channel_layer.group_add(self.room_group_name, self.channel_name)
        await self.accept()
        logger.info(f"User {self.user} connected to {self.room_group_name}")

    async def disconnect(self, close_code):
        await self.channel_layer.group_discard(self.room_group_name, self.channel_name)
        logger.info(f"User {self.user} disconnected from {self.room_group_name}")

    async def receive(self, text_data):
        data = json.loads(text_data)
        message  = data['message']
        group_name = data['group_name']
       

        await self.channel_layer.group_send(
            self.room_group_name,
            {
                'type': 'chat_message',
                'message': message,
                'group_name': group_name,
                
            }
        )

        await self.save_message(
            group_name=self.room_group_name,
            message=message
        )
        logger.info(f"Message from {group_name} saved and sent: {message}")
       
    async def chat_message(self, event):
        message = event['message']
        group_name = event['group_name']
       

        await self.send(text_data=json.dumps({
            'message': message,
            'group_name': group_name,
           
        }))

    @database_sync_to_async
    def save_message(self, group_name, message):
        name, pk = group_name.split('_')
        patient = User.objects.get(pk=pk)
        pharmacist = pharmauser.objects.get(name=name)

        try: 
                
            chatmessages = ChatMessage.objects.create(
            message=message,
            group_name=group_name,
            pharmacist=pharmacist, 
            patient=patient, 
            timestamp=datetime.datetime.now())
            


          
        except (pharmauser.DoesNotExist, User.DoesNotExist) as e:
            logger.error(f"Error saving message: {e}")
