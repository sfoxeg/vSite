from django.urls import path
from chat.views import ChatListView

app_name = 'chat'

urlpatterns = [
    path('', ChatListView.as_view(), name='chat_list'),
    path('id<int:chat_id>', ChatListView.as_view(), name='chat_id'),
    path('gid<int:group_id>?', ChatListView.as_view(), name='chat_gid'),
]
