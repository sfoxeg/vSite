from chat.models import Chat, Message


def get_chat_messages(chat_user_id: int, current_user: object) -> list:
    messages = []
    model_messages = Message.objects.filter(chat=Chat.objects.get(chat_user=chat_user_id))
    for message in model_messages:
        im_sender = True if message.sender == current_user else False
        messages.append({
            'im_sender': im_sender,
            'is_read': message.is_Read,
            'created_at': message.created_at,
            'text': message.text,
        })
    return messages
