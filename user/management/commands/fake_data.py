import random
from faker import Faker
from django.core.management.base import BaseCommand
from user.models import User, UserProfile, Climbing
from utils import CITIES
import os

class Command(BaseCommand):
    help = u'Создание тестовых пользователей со случайным содержанием полей'

    def add_arguments(self, parser):
        parser.add_argument('-c', '--count', type=int, help=u'Количество создаваемых пользователей')

    def create_user(self):
        fake = Faker('ru_RU')
        userprofile = UserProfile(user=User())
        userprofile.goal = random.randrange(1, 4)
        userprofile.city = random.randrange(1, len(CITIES) + 1)
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
        userprofile.climbing = Climbing.objects.get(profile=userprofile)
        userprofile.climbing.bouldering = random.randrange(0, 12)
        userprofile.climbing.leading = random.randrange(0, 12)
        userprofile.climbing.where_bouldering = random.randrange(0, 3)
        userprofile.climbing.where_leading = random.randrange(0, 3)
        userprofile.climbing.belay = random.randrange(0, 3)
        userprofile.climbing.save()
        return f'{first_name} {last_name}..ok'

    def handle(self, *args, **options):
        count = int(options['count'])
        for _ in range(0, count):
            print(f'{_} {self.create_user()}')
