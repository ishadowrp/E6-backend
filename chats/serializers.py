from django.contrib.auth import get_user_model # Для подключения к API пользователей
from rest_framework import serializers
from .models import Chat, Message

class ChatSerializer(serializers.ModelSerializer):
    class Meta:
        fields = ('id', 'owner', 'title', 'chat_users', 'date_created',)
        model = Chat

class MessageSerializer(serializers.ModelSerializer):
    class Meta:
        fields = ('id', 'author', 'chat', 'date_posted', 'content',)
        model = Message

class UserSerializer(serializers.ModelSerializer): # Для подключения к API пользователей
    class Meta:
        model = get_user_model()
        fields = ('id', 'username',)