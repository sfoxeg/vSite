from django.db import models
from user.models import User
from search.models import City


class UserProfile(models.Model):
    GOAL = (
        (0, 'Не в поиске'),
        (1, 'Вместе полазать'),
        (2, 'Больше, чем полазать'),
        (3, 'За любой кипиш'),
    )

    user = models.ForeignKey(to=User, on_delete=models.CASCADE, related_name='profiles', verbose_name='Пользователь')
    goal = models.IntegerField(choices=GOAL, default=0, verbose_name='Цель поиска')
    first_name = models.CharField(max_length=32, blank=False, verbose_name='Имя')
    last_name = models.CharField(max_length=32, blank=False, verbose_name='Фамилия')
    description = models.TextField(blank=True, verbose_name='О себе')
    city = models.ForeignKey(to=City, null=True, on_delete=models.CASCADE, verbose_name='Город')
    height = models.PositiveIntegerField(null=True, blank=True, verbose_name='Рост')
    weight = models.PositiveIntegerField(null=True, blank=True, verbose_name='Вес')
    avatar = models.ImageField(upload_to="static/users_images", blank=True, null=True, verbose_name='Аватар')

    def __name(self):
        return f'{self.first_name} {self.last_name}'

    name = __name

    class Meta:
        db_table = "profiles"
        verbose_name = 'Профиля'
        verbose_name_plural = 'Профили'

    def __str__(self):
        return self.last_name
