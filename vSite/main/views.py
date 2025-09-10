from django.http import HttpResponse
from django.shortcuts import render
from main.models import City
from utils.city_list import city_list


def index(request) -> HttpResponse:
    context = {
        "city": city_list(City),
        "age": range(19, 80)
    }
    return render(request, 'main/main.html', context)
