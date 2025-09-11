from django.http import HttpResponse
from django.shortcuts import render
from user.models import UserProfile
from main.models import City
from utils.city_list import city_list


def index(request) -> HttpResponse:
    names = []
    users = UserProfile.objects.order_by('-id')[:10]
    for usr in users:
        names.append(f'{usr.first_name} {usr.last_name}')

    context = {
        "city": city_list(City),
        "names": names,
        "age": range(18, 80)
    }
    return render(request, 'main/main.html', context)
