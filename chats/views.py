from django.contrib.auth import get_user_model
from rest_framework import viewsets, permissions # new
from .models import Chat, Message
from .permissions import IsAuthorOrReadOnly, IsOwnerOrReadOnly
from .serializers import ChatSerializer, MessageSerializer, UserSerializer

class ChatViewSet(viewsets.ModelViewSet): # new
    permission_classes = (IsOwnerOrReadOnly,)
    queryset = Chat.objects.all()
    serializer_class = ChatSerializer

class MessageViewSet(viewsets.ModelViewSet): # new
    permission_classes = (permissions.IsAuthenticated,)
    queryset = Message.objects.all()
    serializer_class = MessageSerializer

class UserViewSet(viewsets.ModelViewSet): # new
    permission_classes = (permissions.IsAuthenticated,)
    queryset = get_user_model().objects.all()
    serializer_class = UserSerializer