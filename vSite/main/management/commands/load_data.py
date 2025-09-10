from django.core.management.base import BaseCommand
import json
from main.models import City


class Command(BaseCommand):
    def handle(self, *args, **options):
        with open('./start_data/cities.json', 'rb') as f:
            data = json.load(f)

            for _ in data:
                city = City()
                city.name = _
                city.save()
                print(_)
        print('finished')
