from django.core.management.base import BaseCommand
from user.models import User, UserProfile


class Command(BaseCommand):
    help = u'Создание тестовых пользователей'

    def create_user(self, email, password, sex, first_name, last_name):
        profile = UserProfile(user=User())
        profile.user.email = email
        profile.user.set_password(password)
        profile.user.sex = sex
        profile.user.date_of_birth = '1985-01-02'
        profile.user.is_active = True
        profile.user.is_staff = True
        profile.user.is_superuser = True
        profile.first_name = first_name
        profile.last_name = last_name
        profile.goal = 3
        profile.user.save()
        profile.save()
        profile.climbing.belay_description = 'test'
        profile.climbing.save()
        return f'{email}..ok'

    def handle(self, *args, **options):
        test1 = self.create_user(email='test1', password='testpass', sex=False, first_name='Мудила', last_name='Страшный')
        print(test1)
        test2 = self.create_user(email='test2', password='testpass', sex=True, first_name='Баба', last_name='с Возу')
        print(test2)
