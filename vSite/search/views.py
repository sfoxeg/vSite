from django.http import HttpResponse
from django.shortcuts import render
from django.contrib.auth.decorators import login_required


@login_required
def search(request) -> HttpResponse:
    context = {
    }
    return render(request, 'search/main.html', context)
