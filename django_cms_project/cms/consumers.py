from channels.generic.websocket import AsyncWebsocketConsumer, AsyncJsonWebsocketConsumer
import json

class CmsConsumer( AsyncJsonWebsocketConsumer ):
    
    async def connect( self ):
        self.room_name = self.scope[ 'url_route' ][ 'kwargs' ][ 'group_name' ]
        self.room_group_name = 'group_%s' % self.room_name

        await self.channel_layer.group_add(
            self.room_group_name,
            self.channel_name
        )

        await self.accept()
    

    async def disconnect( self, close_code ):
        await self.channel_layer.group_discard(
            self.room_group_name,
            self.channel_name
        )

    async def receive( self, text_data ):
        text_data_json = json.loads( text_data )
        message = text_data_json[ 'message' ]

        await self.channel_layer.group_send(
            self.room_group_name,
            {
                'type': 'send_message',
                'message': message
            }
        )

    async def send_data_planta( self, event ):
        data = event[ 'data_planta' ]

        await self.send( text_data = json.dumps({
            'planta': data
        }))
    