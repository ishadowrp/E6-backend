from django.urls import path
from rest_framework.routers import SimpleRouter
from rest_framework.urlpatterns import format_suffix_patterns
from .views import UserViewSet, ChatViewSet, MessageViewSet, ChatJoinViewSet

router = SimpleRouter()
router.register('users', UserViewSet, basename='users')
router.register('messages', MessageViewSet, basename='messages')
router.register('chats', ChatViewSet, basename='chats')

urlpatterns = router.urls
urlpatterns.append(path('chat/join/<int:pk>/', ChatJoinViewSet.as_view()),)

urlpatterns = format_suffix_patterns(urlpatterns)