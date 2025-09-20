from django.db import models
from django.db.models.signals import post_save
from django.dispatch import receiver
from user.models import UserProfile


class Climbing(models.Model):
    __CATEGORY = (
        (0, 'Нет'),
        (1, '5'),
        (2, '6a/a+'),
        (3, '6b/b+'),
        (4, '6c/c+'),
        (5, '7a/a+'),
        (6, '7b/b'),
        (7, '7c/c+'),
        (8, '8a/a+'),
        (9, '8b/b'),
        (10, '8c/c+'),
        (11, '9 и выше'),
    )
    __WHERE = (
        (0, 'скалы/камни'),
        (1, 'фанера'),
        (2, 'Я за любой движ'),
    )
    __BELAY = (
        (0, "Нет"),
        (1, "Верхняя"),
        (2, "Нижняя и верхняя"),
    )
    profile = models.OneToOneField(to=UserProfile, on_delete=models.CASCADE, related_name='climbing')
    leading = models.IntegerField(choices=__CATEGORY, default=0, verbose_name='Трудность')
    where_leading = models.IntegerField(choices=__WHERE, default=0, verbose_name="Где лазаю трудность")
    bouldering = models.IntegerField(choices=__CATEGORY, default=0, verbose_name='Боулдеринг')
    where_bouldering = models.IntegerField(choices=__WHERE, default=0, verbose_name="Где лазаю боулдеринг")
    alpinism = models.BooleanField(default=False, verbose_name='Альпинизм')
    belay = models.IntegerField(choices=__BELAY, default=0, verbose_name='Верхняя страховка')
    belay_description = models.TextField(blank=True, verbose_name='Примечание о страховке')

    class Meta:
        db_table = "climbing"
        verbose_name = 'Climbing'
        verbose_name_plural = 'Climbing'

    def __str__(self):
        return str(self.id)


@receiver(post_save, sender=UserProfile)
def create_user_profile(sender, instance, created, **kwargs):
    if created:
        Climbing.objects.create(profile=instance)


@receiver(post_save, sender=UserProfile)
def save_user_profile(sender, instance, **kwargs):
    instance.climbing.save()
