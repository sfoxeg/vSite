from django.http import HttpResponse
from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from utils.nav_vars import name, names, cities

@login_required
def search(request) -> HttpResponse:
    context = {
        "name": name(request),
        "city": cities,
        "names": names,
        "age": range(18, 80)
    }
    return render(request, 'search/main.html', context)
