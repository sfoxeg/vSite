from django.contrib.auth.base_user import AbstractBaseUser
from django.db import models
from django.contrib.auth.models import UserManager, PermissionsMixin
from django.utils import timezone


class User(AbstractBaseUser, PermissionsMixin):
    username = None
    email = models.EmailField(max_length=255, unique=True, verbose_name='email address')
    sex = models.BooleanField(default=False, verbose_name='Пол')
    date_of_birth = models.DateField(default=False, verbose_name='Дата рождения')
    is_active = models.BooleanField(default=True, verbose_name='Активный')
    is_staff = models.BooleanField(default=False, verbose_name='Админ')
    is_superuser = models.BooleanField(default=False, verbose_name='Суперюзер')
    date_joined = models.DateTimeField(default=timezone.now)

    objects = UserManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['sex']

    class Meta:
        db_table = "users"
        verbose_name = 'Пользователя'
        verbose_name_plural = 'Пользователи'

    def __str__(self):
        return self.email
