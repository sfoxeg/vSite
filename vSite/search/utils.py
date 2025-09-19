from datetime import datetime
from dateutil.relativedelta import relativedelta
from search.models import City


def date(date_of_birth: str) -> str:
    current_date = datetime.now()
    date_of_birth = str(current_date - relativedelta(years=int(date_of_birth)))
    date_of_birth = datetime.strptime(date_of_birth, '%Y-%m-%d %H:%M:%S.%f')
    return str(date_of_birth)[0:9]


def get_or_session(obj: object, arg_name: str) -> str:
    arg_value = obj.request.GET.get(arg_name)
    if arg_value:
        obj.request.session[arg_name] = arg_value
    return obj.request.session.get(arg_name, '')


def city_list(obj):
    city_list = []
    city = obj.objects.all()
    for _ in city:
        city_list.append({_.id: _.name})
    return city_list


cities = city_list(City)
