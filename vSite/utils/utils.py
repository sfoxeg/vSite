from user.models import UserProfile
from main.models import City


def city_list(obj):
    city_list = []
    city = obj.objects.all()
    for _ in city:
        city_list.append({_.id: _.name})
    return city_list


def name(request):
    if request.user.is_authenticated:
        userprofile = UserProfile.objects.get(user=request.user)
        return f'{userprofile.first_name} {userprofile.last_name}'
    return 'None'


names = []
for usr in UserProfile.objects.order_by('-id')[:10]:
    names.append(f'{usr.first_name} {usr.last_name}')

cities = city_list(City)
