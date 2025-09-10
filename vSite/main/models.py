from django.db import models


class City(models.Model):
    name = models.CharField(max_length=50, unique=True, verbose_name='Город')
