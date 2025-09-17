from django.db import models


class City(models.Model):
    name = models.CharField(max_length=50, unique=True, verbose_name='Город')

    class Meta:
        db_table = "cities"
        verbose_name = 'Города'
        verbose_name_plural = 'Города'

    def __str__(self):
        return self.name
