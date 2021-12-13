from django.contrib.auth import get_user_model
from rest_framework import viewsets, permissions, generics # new
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from django.http import Http404
from .models import Chat, Message
from .permissions import IsUserOrReadOnly, IsOwnerOrReadOnly
from .serializers import ChatSerializer, MessageSerializer, UserSerializer, ChatUserSerializer

class ChatJoinViewSet(APIView):
    permissions_classes = (permissions.IsAuthenticated,)
    serializer_class = ChatUserSerializer

    def get_object(self, pk):
        try:
            return Chat.objects.get(pk=pk)
        except Chat.DoesNotExist:
            raise Http404

    def get(self, request, pk):
        chat = self.get_object(pk)
        messages = Message.objects.filter(chat__id=pk)

        listOfMessage = []
        for item in messages:
            dictMessage = {'author': item.author.id, 'date_posted': item.date_posted, 'content': item.content}
            listOfMessage.append(dictMessage)

        listMembers = []
        for usr in chat.chat_users.all():
            listMembers.append({'id': usr.id, 'username': usr.username})

        dictResponse = {'chat': pk, 'chat_users': listMembers, 'messages': listOfMessage}

        return Response(dictResponse)

    def put(self, request, pk):
        chat = self.get_object(pk)
        chat.chat_users.add(request.user)
        return Response({'status': 'ok'})

class ChatViewSet(viewsets.ModelViewSet): # new
    permission_classes = (IsOwnerOrReadOnly, permissions.IsAuthenticated,)
    queryset = Chat.objects.all()
    serializer_class = ChatSerializer

    def perform_create(self, serializer):
        # here you will send `created_by` in the `validated_data`
        first_member_list = []
        first_member_list.append(self.request.user)
        serializer.save(owner=self.request.user, chat_users = first_member_list)

class MessageViewSet(viewsets.ModelViewSet): # new
    permission_classes = (permissions.IsAuthenticated,)
    queryset = Message.objects.all()
    serializer_class = MessageSerializer

    def perform_create(self, serializer):
        serializer.save(author=self.request.user)


class UserViewSet(viewsets.ModelViewSet): # new
    permission_classes = (IsUserOrReadOnly, permissions.IsAuthenticated,)
    queryset = get_user_model().objects.all()
    serializer_class = UserSerializer