from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import ListView
from django.urls import reverse_lazy
from user.models import UserProfile, Climbing
from search.utils import cities, get_or_session, date


class SearchView(LoginRequiredMixin, ListView):
    template_name = 'search/main.html'
    model = UserProfile
    context_object_name = 'profiles'
    success_url = reverse_lazy('search:search')
    paginate_by = 8

    def get_queryset(self):
        looking_for = get_or_session(self, 'looking_for')
        goal = get_or_session(self, 'goal')
        age_min = get_or_session(self, 'age_min')
        age_max = get_or_session(self, 'age_max')
        city = get_or_session(self, 'city')

        leading = get_or_session(self, 'leading')
        where_leading = get_or_session(self, 'where_leading')
        bouldering = get_or_session(self, 'bouldering')
        where_bouldering = get_or_session(self, 'where_bouldering')
        speed = self.request.GET.get('speed', False)
        alpinism = self.request.GET.get('alpinism', False)
        belay = get_or_session(self, 'belay')

        order = get_or_session(self, 'order')

        if order == 'oldest':
            order = "user__date_of_birth"
        elif order == 'youngest':
            order = "-user__date_of_birth"
        else:
            order = "-user__last_login"

        if looking_for:
            profiles = super().get_queryset()
            profiles = (profiles
                        .filter(user__is_active=True)
                        .filter(city=city)
                        .filter(user__date_of_birth__range=(date(age_max), date(age_min)))
                        .order_by(order))

            if int(goal) < 3:
                profiles = profiles.filter(goal=goal)

            if looking_for == 'male':
                profiles = profiles.filter(user__sex=False)
            elif looking_for == 'female':
                profiles = profiles.filter(user__sex=True)

            if int(leading) > 0:
                profiles = profiles.filter(climbing__leading__gte=leading)
                if int(where_leading) < 2:
                    profiles = profiles.filter(climbing__where_leading=where_leading) | profiles.filter(climbing__where_leading=2)

            if int(bouldering) > 0:
                profiles = profiles.filter(climbing__bouldering__gte=bouldering)
                if int(where_bouldering) < 2:
                    profiles = profiles.filter(climbing__where_bouldering=where_bouldering) | profiles.filter(climbing__where_bouldering=2)

            if int(belay) > 0:
                profiles = profiles.filter(climbing__belay=belay)

            if speed == 'True':
                profiles = profiles.filter(climbing__speed=True)

            if alpinism == 'True':
                profiles = profiles.filter(climbing__alpinism=True)

            return profiles
        return []

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["title"] = 'Поиск'
        context["looking_for"] = get_or_session(self, 'looking_for')
        context["goal"] = get_or_session(self, 'goal')
        context["age_min"] = get_or_session(self, 'age_min')
        context["age_max"] = get_or_session(self, 'age_max')
        context["city"] = get_or_session(self, 'city')

        context["leading"] = get_or_session(self, 'leading')
        context["where_leading"] = get_or_session(self, 'where_leading')
        context["bouldering"] = get_or_session(self, 'bouldering')
        context["where_bouldering"] = get_or_session(self, 'where_bouldering')
        context["speed"] = self.request.GET.get('speed', False)
        context["alpinism"] = self.request.GET.get('alpinism', False)
        context["belay"] = get_or_session(self, 'belay')
        context["order"] = get_or_session(self, 'order')
        context["age"] = range(18, 81)
        context["cities"] = cities
        return context
