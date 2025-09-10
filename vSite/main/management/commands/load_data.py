from django.core.management.base import BaseCommand
import json
from main.models import City


class Command(BaseCommand):
    def handle(self, *args, **options):
        with open('./start_data/cities.json', 'rb') as f:
            data = json.load(f)

            for i in data:
                print(i)
                city = City()
                city.name = i
                city.save()
        print('finished')
