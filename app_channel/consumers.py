from channels.generic.websocket import WebsocketConsumer
from asgiref.sync import async_to_sync
import json
from channels.generic.websocket import AsyncJsonWebsocketConsumer


class TestConsumer(WebsocketConsumer):
    # ws://
    def connect(self):
        self.room_name = "test_consumer"
        self.room_group_name = "test_consumer_group"
        async_to_sync(self.channel_layer.group_add)(
            self.room_group_name, self.channel_name
        )
        self.accept()
        self.send(text_data=json.dumps({"status": "Connected from channel"}))

    # {'user_id' :1 , "message":"hii"}
    def receive(self, text_data):
        print(text_data)
        # self.send(text_data = json.dumps(
        #     text_data
        # ))

        self.send(text_data=json.dumps({"status": "we got you"}))

    def disconnect(self, *args, **kwargs):
        print("disconnected")

    def send_notifications(self, event):
        print("send_notification")
        data = json.loads(event.get("value"))
        
        self.send(text_data=json.dumps({"payload": data}))

        print("send_notification")


class NewConsumer(AsyncJsonWebsocketConsumer):
    async def connect(self):
        self.room_name = "new_consumer"
        self.room_group_name = "new_consumer_group"

        await (self.channel_layer.group_add)(
            self.room_group_name, 
            self.channel_name
            )

        await self.accept()
        await self.send(
            text_data=json.dumps({"status": "connect from new async json consumer"})
        )

    async def receive(self, text_data):
        print(text_data)
        await self.send(text_data=json.dumps({"status": "we got new consumer "}))

    async def disconnect(self, *args, **kwargs):
        print("disconnect")

    async def send_notifications(self, event):
     
        data = json.loads(event.get("value"))
        await self.send(text_data=json.dumps({"payload": data}))
