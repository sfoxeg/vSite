from django.db import models


class Climbing(models.Model):
    CATEGORY = (
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
    WHERE = (
        (0, 'скалы/камни'),
        (1, 'фанера'),
        (2, 'Я за любой движ'),
    )

    difficulty = models.IntegerField(choices=CATEGORY, default=0, verbose_name='Сложность')
    where_difficulty = models.IntegerField(choices=WHERE, default=0, verbose_name="Где лазаю сложность")
    bouldering = models.IntegerField(choices=CATEGORY, default=0, verbose_name='Боулдеринг')
    where_bouldering = models.IntegerField(choices=WHERE, default=0, verbose_name="Где лазаю боулдеринг")
    faster = models.BooleanField(default=False, verbose_name='Скорость')
    alpinism = models.BooleanField(default=False, verbose_name='Альпинизм')
    belay_up = models.BooleanField(default=False, verbose_name='Верхняя страховка')
    belay_down = models.BooleanField(default=False, verbose_name='Нижняя страховка')
    belay_description = models.TextField(blank=True, verbose_name='Примечание о страховке')

    class Meta:
        db_table = "climbing"
        verbose_name = 'Climbing'
        verbose_name_plural = 'Climbing'

    def __str__(self):
        return str(self.id)
