from django.urls import path
from user.views.view_login import login
from user.views.view_register import register
from user.views.view_logout import logout
from user.views.view_profile import profile


app_name = 'user'

urlpatterns = [
    path('login/', login, name='login'),
    path('register/', register, name='register'),
    path('logout/', logout, name='logout'),
    path('profile/', profile, name='profile')
]
