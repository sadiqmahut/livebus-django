import json
from channels.generic.websocket import WebsocketConsumer
from asgiref.sync import async_to_sync
from .models import Buses, Stops

class BusConsumer(WebsocketConsumer):
    def connect(self):
        self.room_name = self.scope['url_route']['kwargs']['bunq']
        self.room_group_name = 'bus_%s' % self.room_name
        async_to_sync(self.channel_layer.group_add)(
            self.room_group_name,
            self.channel_name
        )
        self.accept()

    def disconnect(self, close_code):
        async_to_sync(self.channel_layer.group_discard)(
            self.room_group_name,
            self.channel_name
        )

    def receive(self, text_data):
        async_to_sync(self.channel_layer.group_send)(
            self.room_group_name,
            {
                'type': 'update_stop',
                'message': text_data
            }
        )

    def update_stop(self, message):
        data = json.loads(message['message'])
        s = Stops.objects.get(sname = data['stop'])
        Buses.objects.filter(broute = data['r']).update(b_cur_stop=s)
        self.send(text_data=json.dumps({
            'message': s.sname
        }))
        print(data)
