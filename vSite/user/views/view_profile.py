from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
from django.shortcuts import render


@login_required
def profile(request) -> HttpResponse:
    return render(request, 'user/profile.html')
