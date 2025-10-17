from chat.models import Chat, ChatUser, Message


def get_chat_list(user: object) -> list:
    chat_type = None
    url = None
    chats = []

    for chat in Chat.objects.filter(chat_user__user=user).order_by('-id'):
        users = []
        chat_users = ChatUser.objects.filter(chat=chat)
        for chat_user in chat_users:
            if chat_user.user != user:
                if chat_users.count() > 2:
                    chat_type = 'group'
                    url = chat.id
                else:
                    chat_type = 'chat'
                    url = chat_user.user.id
                    ava = chat_user.user.profile.avatar
                users.append(f'{chat_user.user.profile.first_name} {chat_user.user.profile.last_name}')

        message = Message.objects.filter(chat=chat).last()
        if message:
            last_message = 'Вы: ' + message.text if message.sender == user else message.text
            is_read = message.is_Read
            created_at = message.created_at

            chats.append({
                'type': chat_type,
                'url': url,
                'name': chat.name,
                'ava': ava,
                'users': users,
                'last_message': last_message,
                'is_read': is_read,
                'created_at': created_at,
            })
    return chats
