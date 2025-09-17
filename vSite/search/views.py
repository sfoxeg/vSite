from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import ListView
from user.models.model_user_profile import UserProfile


class SearchView(LoginRequiredMixin, ListView):
    template_name = 'search/main.html'
    model = UserProfile
    context_object_name = 'profiles'
    paginate_by = 8

    def get_context_data(self, **kwargs):
        cotext = super().get_context_data(**kwargs)
        cotext["age"] = range(18, 80)
        return cotext
