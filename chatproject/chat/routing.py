from django.urls import path
from . import consumers

ASGI_urlpatterns = [
    path("websocket/<str:you>/<str:username>", consumers.ChatConsumer.as_asgi()),
]