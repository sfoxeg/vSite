from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import DetailView
from user.forms import UserProfileForm
from search.utils import cities, get_or_session
from user.models import UserProfile


class UserIdView(LoginRequiredMixin, DetailView):
    template_name = 'user/main.html'
    slug_url_kwarg = 'profile_id'
    context_object_name = 'profile'

    def get_object(self, queryset=None):
        return UserProfile.objects.get(id=self.kwargs.get(self.slug_url_kwarg))

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["title"] = self.object.name
        context["profile_type"] = 'id'
        context["looking_for"] = get_or_session(self, 'looking_for')
        context["goal"] = get_or_session(self, 'goal')
        context["age_min"] = get_or_session(self, 'age_min')
        context["age_max"] = get_or_session(self, 'age_max')
        context["city"] = get_or_session(self, 'city')
        context["order"] = get_or_session(self, 'order')
        context["cities"] = cities
        context["age"] = range(18, 81)
        return context
