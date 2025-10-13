from django.db import models
from django.utils import timezone


class Chat(models.Model):
    name = models.CharField(default='')
    created_at = models.DateTimeField(default=timezone.now)

    class Meta:
        db_table = "chats"
        verbose_name = 'Чат'
        verbose_name_plural = 'Чаты'
