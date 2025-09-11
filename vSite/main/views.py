from django.http import HttpResponse
from django.shortcuts import render
from utils.nav_vars import name, names, cities


def index(request) -> HttpResponse:
    context = {
        "name": name(request),
        "city": cities,
        "names": names,
        "age": range(18, 80)
    }
    return render(request, 'main/main.html', context)
