from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from django.views.generic import ListView
from chat.models import Message


class ChatListView(LoginRequiredMixin, ListView):
    model = Message
    context_object_name = 'profiles'
    success_url = reverse_lazy('chats:chat')
    paginate_by = 8
