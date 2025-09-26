from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from django.contrib import messages
from django.views.generic import UpdateView
from user.forms import UserProfileForm
from search.utils import cities, get_or_session


class UserProfileAccountView(LoginRequiredMixin, UpdateView):
    template_name = 'user/main.html'
    form_class = UserProfileForm
    success_url = reverse_lazy('user:profile')
    context_object_name = 'profile'

    def get_object(self, queryset=None):
        return self.request.user

    def form_valid(self, form):
        messages.success(self.request, "Профиль изменен")
        return super().form_valid(form)

    def form_invalid(self, form):
        messages.warning(self.request, "Что-то пошло не так")
        return super().form_invalid(form)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["title"] = self.object.profile.name
        context["profile_type"] = 'account'
        context["looking_for"] = get_or_session(self, 'looking_for')
        context["goal"] = get_or_session(self, 'goal')
        context["age_min"] = get_or_session(self, 'age_min')
        context["age_max"] = get_or_session(self, 'age_max')
        context["city"] = get_or_session(self, 'city')
        context["order"] = get_or_session(self, 'order')
        context["cities"] = cities
        context["age"] = range(18, 81)
        return context
