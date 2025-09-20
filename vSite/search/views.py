from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import ListView
from django.urls import reverse_lazy
from user.models.model_user_profile import UserProfile
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
                        .filter(goal=goal)
                        .filter(city__id=city)
                        .filter(user__date_of_birth__range=(date(age_max), date(age_min)))
                        .order_by(order))

            if looking_for == 'male':
                profiles = profiles.filter(user__sex=False)
            elif looking_for == 'female':
                profiles = profiles.filter(user__sex=True)

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
        context["order"] = get_or_session(self, 'order')
        context["age"] = range(18, 81)
        context["cities"] = cities
        return context
