from django.urls import path

from user.views import UserLoginView, UserRegistrationView, UserProfileView, UserProfileClimbingView, UserIdView, \
    logout, UserProfileAccountView

app_name = 'user'

urlpatterns = [
    path('login', UserLoginView.as_view(), name='login'),
    path('registration', UserRegistrationView.as_view(), name='registration'),
    path('logout', logout, name='logout'),
    path('', UserProfileView.as_view(), name='profile'),
    path('climbing', UserProfileClimbingView.as_view(), name='climbing'),
    path('account', UserProfileAccountView.as_view(), name='account'),
    path('id<int:profile_id>', UserIdView.as_view(), name='id')
]
