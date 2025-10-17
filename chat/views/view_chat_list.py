import logging
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import TemplateView

from chat.models import Chat, ChatUser, Message


class ChatListView(LoginRequiredMixin, TemplateView):
    logging.basicConfig(level=logging.DEBUG)

    template_name = 'chat/chat_list.html'

    def get_context_data(self, **kwargs):
        chat_type = None
        url = None
        chats = []
        model_chats = Chat.objects.filter(chat_user__user=self.request.user).order_by('-id')

        for chat in model_chats:
            users = []
            chat_users = ChatUser.objects.filter(chat=chat)
            for chat_user in chat_users:
                if chat_user.user != self.request.user:
                    if chat_users.count() > 2:
                        chat_type = 'group'
                        url = chat.id
                    else:
                        chat_type = 'chat'
                        url = chat_user.user.id
                    users.append(f'{chat_user.user.profile.first_name} {chat_user.user.profile.last_name}')

            message = Message.objects.filter(chat=chat).last()
            if message:
                last_message = 'Вы: ' + message.text if message.sender == self.request.user else message.text
                is_read = message.is_Read
                created_at = message.created_at

                chats.append({
                    'type': chat_type,
                    'url': url,
                    'name': chat.name,
                    'users': users,
                    'last_message': last_message,
                    'is_read': is_read,
                    'created_at': created_at,
                })

        # logging.debug(chats)

        if 'chat_id' in self.kwargs:
            logging.debug(self.kwargs['chat_id'])

        context = super().get_context_data(**kwargs)
        context["title"] = 'Сообщения'
        context["chats"] = chats
        return context
