from django.contrib.auth.base_user import AbstractBaseUser
from django.db import models
from django.contrib.auth.models import UserManager, PermissionsMixin
from django.utils import timezone
from datetime import datetime


class User(AbstractBaseUser, PermissionsMixin):
    __SEX = (
        (False, 'Мужчина'),
        (True, 'Женщина')
    )
    username = None
    email = models.EmailField(max_length=255, unique=True, verbose_name='email address')
    sex = models.BooleanField(choices=__SEX, default=False, verbose_name='Пол')
    date_of_birth = models.DateField(default=False, verbose_name='Дата рождения')
    is_active = models.BooleanField(default=True, verbose_name='Активный')
    is_staff = models.BooleanField(default=False, verbose_name='Админ')
    is_superuser = models.BooleanField(default=False, verbose_name='Суперюзер')
    date_joined = models.DateTimeField(default=timezone.now)

    objects = UserManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['sex']

    def __age(self) -> int:
        today = datetime.now().date()
        age = today.year - self.date_of_birth.year - (
                (today.month, today.day) < (self.date_of_birth.month, self.date_of_birth.day))
        # Не забываем о днях рождения, приходящихся на високосный день каждые четыре года!
        if self.date_of_birth.month == 2 and self.date_of_birth.day == 29:
            try:
                leap_year_birthday = self.date_of_birth.replace(year=today.year)
            except ValueError:
                # Если в этом году нет 29 февраля, празднование происходит 28 февраля
                leap_year_birthday = self.date_of_birth.replace(year=today.year, day=28)

            if today < leap_year_birthday:
                age -= 1  # Отмечаем эту дату заново, время для празднования ещё не пришло!
        return age

    age = __age

    class Meta:
        db_table = "users"
        verbose_name = 'Пользователя'
        verbose_name_plural = 'Пользователи'

    def __str__(self):
        return self.email
