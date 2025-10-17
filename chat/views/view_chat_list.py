from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import TemplateView
import logging
from chat.utils import get_chat_list, get_chat_messages

class ChatListView(LoginRequiredMixin, TemplateView):
    template_name = 'chat/chat_list.html'

    def get_context_data(self, **kwargs):
        messages = []
        chats = get_chat_list(user=self.request.user)
        if 'chat_id' in self.kwargs:
            messages = get_chat_messages(current_user=self.request.user, chat_user_id=self.kwargs['chat_id'],)
            logging.debug(self.kwargs['chat_id'])

        context = super().get_context_data(**kwargs)
        context["title"] = 'Сообщения'
        context["chats"] = chats
        context["messages"] = messages
        return context
