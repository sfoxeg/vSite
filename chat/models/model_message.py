from django.db import models
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.utils import timezone
from chat.models import Chat
from user.models import User


class Message(models.Model):
    chat = models.ForeignKey(to=Chat, on_delete=models.CASCADE, related_name='chat_message')
    sender = models.ForeignKey(to=User, on_delete=models.CASCADE, related_name='from_user')
    is_Read = models.BooleanField(default=False)
    created_at = models.DateTimeField(default=timezone.now)
    text = models.TextField(blank=True, verbose_name='Текст')

    class Meta:
        db_table = "messages"
        verbose_name = 'Сообщение'
        verbose_name_plural = 'Сообщения'


@receiver(post_save, sender=Message)
def added_new_message(sender, instance, created, **kwargs):
    if created:
        # Сигнал для отправки сообщения в чат
        pass
