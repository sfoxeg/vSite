from django.http import HttpResponse
from django.shortcuts import render
from user.forms import UserRegistrationForm


def register(request) -> HttpResponse:
    if request.method == 'POST':
        print(request.POST)
        form = UserRegistrationForm(data=request.POST)
        if form.is_valid():
            form.save()
    else:
        form = UserRegistrationForm()

    context = {
        'form': form
    }
    return render(request, 'user/register.html', context)
