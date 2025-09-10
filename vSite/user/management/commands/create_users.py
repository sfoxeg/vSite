from django.core.management.base import BaseCommand
from user.models import User


class Command(BaseCommand):
    def create_user(self, email, password, sex):
        user = User()
        user.email = email
        user.set_password(password)
        user.sex = sex
        user.date_of_birth = '1985-01-02'
        user.is_active = True
        user.is_staff = True
        user.is_superuser = True
        user.save()
        return f'{email}..ok'

    def handle(self, *args, **options):
        test1 = self.create_user(email='test1', password='testpass', sex=False)
        print(test1)
        test2 = self.create_user(email='test2', password='testpass', sex=True)
        print(test2)
