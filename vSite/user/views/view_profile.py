from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
from django.shortcuts import render
from main.models import City
from utils.city_list import city_list


@login_required
def profile(request) -> HttpResponse:
    context = {
        "city": city_list(City)
    }
    return render(request, 'user/profile.html', context)
