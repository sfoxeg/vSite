from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
from django.shortcuts import render
from user.models import UserProfile
from main.models import City
from utils import cities


@login_required
def profile(request) -> HttpResponse:
    userprofile = UserProfile.objects.get(user=request.user)

    context = {
        "cities": cities,
        "avatar": userprofile.avatar,
        "name": f'{userprofile.first_name} {userprofile.last_name}',
        "sex": request.user.sex,
        "height": userprofile.height,
        "weight": userprofile.weight,
        "age": request.user.age(),
        "date_of_birth": request.user.date_of_birth,
        "city": userprofile.city.id,
        "description": userprofile.description
    }
    return render(request, 'user/profile.html', context)
