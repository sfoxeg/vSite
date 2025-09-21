from django.urls import path

from user.views import UserLoginView, UserRegistrationView, UserProfileView, UserIdView, logout

app_name = 'user'

urlpatterns = [
    path('login', UserLoginView.as_view(), name='login'),
    path('registration', UserRegistrationView.as_view(), name='registration'),
    path('logout', logout, name='logout'),
    path('', UserProfileView.as_view(), name='profile'),
    path('id<int:profile_id>', UserIdView.as_view(), name='id')
]
