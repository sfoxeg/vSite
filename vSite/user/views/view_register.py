from django.http import HttpResponse
from django.shortcuts import render


def register(request) -> HttpResponse:
    return render(request, 'user/register.html')
