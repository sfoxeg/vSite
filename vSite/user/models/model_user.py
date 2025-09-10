from django.contrib.auth.base_user import AbstractBaseUser
from django.db import models
from django.contrib.auth.models import UserManager


class User(AbstractBaseUser):
    username = None
    email = models.EmailField(max_length=255, unique=True, verbose_name='email address')
    sex = models.BooleanField(default=False, verbose_name='Пол')
    date_of_birth = models.DateField(default=False, verbose_name='Дата рождения')
    is_active = models.BooleanField(default=True, verbose_name='Активный')
    is_admin = models.BooleanField(default=False, verbose_name='Админ')
    avatar = models.ImageField(upload_to="static/users_images", blank=True, null=True, verbose_name='Аватар')

    objects = UserManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['sex']

    class Meta:
        db_table = "users"
        verbose_name = 'Пользователя'
        verbose_name_plural = 'Пользователи'

    def __str__(self):
        return self.email
