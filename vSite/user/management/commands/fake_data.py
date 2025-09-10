from faker import Faker
from django.core.management.base import BaseCommand
from user.models import User, UserProfile


class Command(BaseCommand):
    help = u'Создание тестовых пользователей со случайным содержанием полей'

    def add_arguments(self, parser):
        parser.add_argument('-c', '--count', type=int, help=u'Количество создаваемых пользователей')

    def create_user(self):
        fake = Faker()

        user = User()
        userprofile = UserProfile(user=user)
        userprofile.user.email = fake.email()
        userprofile.user.set_password(fake.password())
        userprofile.user.date_of_birth = fake.date_of_birth()
        sex = fake.boolean()
        userprofile.user.sex = sex
        userprofile.description = fake.text()
        userprofile.height = fake.random_int(150, 192)
        userprofile.weight = fake.random_int(40, 120)
        if sex:
            first_name = fake.first_name_female()
            last_name = fake.last_name_female()
        else:
            first_name = fake.first_name_male()
            last_name = fake.last_name_male()
        userprofile.first_name = first_name
        userprofile.last_name = last_name
        userprofile.user.save()
        userprofile.save()
        return f'{first_name} {last_name}..ok'

    def handle(self, *args, **options):
        count = int(options['count'])
        for _ in range(0, count):
            print(self.create_user())
