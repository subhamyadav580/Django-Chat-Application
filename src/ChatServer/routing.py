from channels.auth import AuthMiddlewareStack
from channels.routing import ProtocolTypeRouter, URLRouter
from channels.security.websocket import AllowedHostsOriginValidator
from django.urls import path, re_path

from chat.consumers import ChatConsumer
from public_chat.consumers import *



application = ProtocolTypeRouter({
	'websocket': AllowedHostsOriginValidator(
		AuthMiddlewareStack(
			URLRouter([
					path('chat/<room_id>/', ChatConsumer),
					path('public_chat/<room_id>/', PublicChatConsumer),
			])
		)
	),
})