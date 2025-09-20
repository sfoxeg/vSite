from django.db import models
from django.db.models.signals import post_save
from django.dispatch import receiver
from user.models import User, Climbing
from utils import CITIES


class UserProfile(models.Model):
    GOAL = (
        (0, 'Не в поиске'),
        (1, 'Вместе полазать'),
        (2, 'Больше, чем полазать'),
        (3, 'За любой кипиш'),
    )
    user = models.OneToOneField(to=User, on_delete=models.CASCADE, related_name='profile', primary_key=True, verbose_name='Пользователь')
    climbing = models.OneToOneField(Climbing, on_delete=models.CASCADE, related_name='profile')
    goal = models.IntegerField(choices=GOAL, default=0, verbose_name='Цель поиска')
    first_name = models.CharField(max_length=32, blank=False, verbose_name='Имя')
    last_name = models.CharField(max_length=32, blank=False, verbose_name='Фамилия')
    description = models.TextField(blank=True, verbose_name='О себе')
    city = models.IntegerField(choices=CITIES, null=True, verbose_name='Город')
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


@receiver(post_save, sender=User)
def create_user_profile(sender, instance, created, **kwargs):
    if created:
        UserProfile.objects.create(user=instance, climbing=Climbing.objects.create())


@receiver(post_save, sender=User)
def save_user_profile(sender, instance, **kwargs):
    instance.profile.climbing.save()
    instance.profile.save()
