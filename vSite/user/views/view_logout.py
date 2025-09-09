from django.contrib import auth
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse


@login_required
def logout(request) -> HttpResponse:
    auth.logout(request)
    return HttpResponseRedirect(reverse('main:index'))
