from django.db import models
from django.utils import timezone
from chat.models import Chat
from user.models import User


class ChatUser(models.Model):
    chat = models.ForeignKey(to=Chat, on_delete=models.CASCADE, related_name='chat_user')
    user = models.ForeignKey(to=User, on_delete=models.CASCADE, related_name='user')
    joined = models.DateTimeField(default=timezone.now)

    class Meta:
        db_table = "chat_users"
        verbose_name = 'Пользователь'
        verbose_name_plural = 'Пользователи'
