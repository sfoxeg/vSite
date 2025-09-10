def city_list(obj):
    city_list = []
    city = obj.objects.all()
    for _ in city:
        city_list.append({_.id: _.name})
    return city_list
