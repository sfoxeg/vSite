from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse
from user.forms import UserRegistrationForm


def register(request) -> HttpResponse:
    if request.method == 'POST':
        print(request.POST)
        form = UserRegistrationForm(data=request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('user:login'))
    else:
        form = UserRegistrationForm()

    context = {
        'form': form
    }
    return render(request, 'user/register.html', context)
