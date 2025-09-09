from django.contrib.auth.decorators import login_required
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from django.contrib import auth
from django.urls import reverse
from user.forms import UserLoginForm


def login(request) -> HttpResponse:
    if request.method == 'POST':
        form = UserLoginForm(data=request.POST)
        if form.is_valid():
            username = request.POST['username']
            password = request.POST['password']
            user = auth.authenticate(username=username, password=password)
            if user:
                auth.login(request, user)
                return HttpResponseRedirect(reverse('main:index'))
    else:
        form = UserLoginForm()

    context = {
        'form': form
    }
    return render(request, 'user/login.html', context)


def register(request) -> HttpResponse:
    return render(request, 'user/register.html')

@login_required
def logout(request) -> HttpResponse:
    auth.logout(request)
    return HttpResponseRedirect(reverse('main:index'))

@login_required
def profile(request) -> HttpResponse:
    return render(request, 'user/profile.html')