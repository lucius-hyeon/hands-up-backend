from django.urls import path

from . import consumers#, read_only

websocket_urlpatterns = [
    path('ws/auction/<int:goods_id>/', consumers.ChatConsumer.as_asgi()),
    path('ws/chat/<int:goods_id>/', consumers.ChatConsumerDirect.as_asgi()),
    path('ws/alram/', consumers.AlramConsumer.as_asgi()),
]