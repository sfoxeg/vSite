from user.models import UserProfile
from main.models import City
from utils.city_list import city_list


def name(request):
    userprofile = UserProfile.objects.get(user=request.user)
    return f'{userprofile.first_name} {userprofile.last_name}'

names = []
for usr in UserProfile.objects.order_by('-id')[:10]:
    names.append(f'{usr.first_name} {usr.last_name}')

cities = city_list(City)