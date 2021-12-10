from django.urls import path
from rest_framework.routers import SimpleRouter
from .views import UserViewSet, ChatViewSet, MessageViewSet

router = SimpleRouter()
router.register('users', UserViewSet, basename='users')
router.register('messages', MessageViewSet, basename='messages')
router.register('', ChatViewSet, basename='chats')

urlpatterns = router.urls