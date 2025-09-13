from django.urls import path

from user.views import UserLoginView, UserRegistrationView, logout, profile

app_name = 'user'

urlpatterns = [
    path('login', UserLoginView.as_view(), name='login'),
    path('registration', UserRegistrationView.as_view(), name='registration'),
    path('logout', logout, name='logout'),
    path('', profile, name='profile')
]
