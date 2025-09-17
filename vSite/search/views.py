from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import ListView
from django.urls import reverse_lazy
import datetime

from dateutil.relativedelta import relativedelta
from user.models.model_user_profile import UserProfile
from search.utils import cities


def date(date: str) -> str:
    current_date = datetime.datetime.now()
    date = str(current_date - relativedelta(years=int(date)))
    date = datetime.datetime.strptime(date, '%Y-%m-%d %H:%M:%S.%f')
    return str(date)[0:9]


class SearchView(LoginRequiredMixin, ListView):
    template_name = 'search/main.html'
    model = UserProfile
    context_object_name = 'profiles'
    success_url = reverse_lazy('search:search')
    paginate_by = 8

    def get_queryset(self):
        looking_for = self.request.GET.get('looking_for')
        age_min = self.request.GET.get('age_min')
        age_max = self.request.GET.get('age_max')
        city = self.request.GET.get('city')

        if city:
            profiles = super().get_queryset()

            profiles = (profiles.filter(user__is_active=True) &
                        profiles.filter(acting=False) &
                        profiles.filter(city__id=city))

            if looking_for == 'male':
                profiles = profiles.filter(user__sex=False)
            elif looking_for == 'female':
                profiles = profiles.filter(user__sex=True)

            if age_min:
                profiles = profiles.filter(user__date_of_birth__range=(date(age_max), date(age_min)))
            return profiles
        return []

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["age"] = range(18, 80)
        context["cities"] = cities
        return context
