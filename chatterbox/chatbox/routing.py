from django.urls import path
from . import consumers

####

websocket_urlpatterns = [
    path('ws/<str:chatbox_name>/', consumers.ChatConsumer.as_asgi()),
]