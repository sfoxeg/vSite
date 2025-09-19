import random
from faker import Faker
from django.core.management.base import BaseCommand
from user.models import User, UserProfile
from search.models import City


class Command(BaseCommand):
    help = u'Создание тестовых пользователей со случайным содержанием полей'

    def add_arguments(self, parser):
        parser.add_argument('-c', '--count', type=int, help=u'Количество создаваемых пользователей')

    def create_user(self):
        fake = Faker('ru_RU')
        userprofile = UserProfile(user=User())

        city = random.randrange(1, 3)
        userprofile.city = City.objects.get(id=city)
        userprofile.user.email = fake.email()
        userprofile.user.set_password(fake.password())
        userprofile.user.date_of_birth = fake.date_of_birth()
        userprofile.description = fake.text()
        userprofile.height = fake.random_int(150, 192)
        userprofile.weight = fake.random_int(40, 120)
        userprofile.user.sex = fake.boolean()
        first_name = fake.first_name_female() if userprofile.user.sex else fake.first_name_male()
        last_name = fake.last_name_female() if userprofile.user.sex else fake.last_name_male()
        userprofile.first_name = first_name
        userprofile.last_name = last_name
        image_bytes_jpeg = fake.image(size=(640, 640), image_format='jpeg')
        with open(f"static/users_images/{first_name}-{last_name}.jpg", "wb") as f:
            f.write(image_bytes_jpeg)
        userprofile.avatar = f"static/users_images/{first_name}-{last_name}.jpg"
        userprofile.user.save()
        userprofile.save()
        return f'{first_name} {last_name}..ok'

    def handle(self, *args, **options):
        count = int(options['count'])
        for _ in range(0, count):
            print(self.create_user())
