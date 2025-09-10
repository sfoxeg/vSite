from django.db import models

from user.models import User
from main.models import City


class UserProfile(models.Model):
    user = models.ForeignKey(to=User, on_delete=models.CASCADE, verbose_name='Пользователь')
    acting = models.BooleanField(default=False, null=False, verbose_name='Поиск разрешен')
    first_name = models.TextField(verbose_name='Имя')
    last_name = models.TextField(verbose_name='Фамилия')
    city = models.ForeignKey(to=City, null=True, on_delete=models.CASCADE, verbose_name='Город')
    height = models.IntegerField(null=False, verbose_name='Рост')
    weight = models.IntegerField(null=False, verbose_name='Вес')
