from django.db import models

from user.models import User
from main.models import City


class UserProfile(models.Model):
    user = models.ForeignKey(to=User, on_delete=models.CASCADE, verbose_name='Пользователь')
    acting = models.BooleanField(default=False, null=False, verbose_name='Поиск разрешен')
    first_name = models.CharField(max_length=32, verbose_name='Имя')
    last_name = models.CharField(max_length=32, verbose_name='Фамилия')
    description = models.TextField(blank=True, verbose_name='О себе')
    city = models.ForeignKey(to=City, null=True, on_delete=models.CASCADE, verbose_name='Город')
    height = models.PositiveIntegerField(null=False, verbose_name='Рост')
    weight = models.PositiveIntegerField(null=False, verbose_name='Вес')
    avatar = models.ImageField(upload_to="static/users_images", blank=True, null=True, verbose_name='Аватар')

    class Meta:
        db_table = "profiles"
        verbose_name = 'Профиля'
        verbose_name_plural = 'Профили'

    def __str__(self):
        return self.last_name
