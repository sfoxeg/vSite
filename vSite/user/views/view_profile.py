from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from django.contrib import messages
from django.views.generic import UpdateView
from user.forms import UserProfileForm
from search.utils import cities
from user.models import UserProfile


class UserProfileView(LoginRequiredMixin, UpdateView):
    template_name = 'user/profile.html'
    form_class = UserProfileForm
    success_url = reverse_lazy('user:profile')

    def get_object(self, queryset=None):
        return UserProfile.objects.get(user=self.request.user)

    def form_valid(self, form):
        messages.success(self.request, "Профиль изменен")
        return super().form_valid(form)

    def form_invalid(self, form):
        messages.warning(self.request, "Что-то пошло не так")
        return super().form_invalid(form)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["cities"] = cities
        context["age"] = range(18, 80)
        return context
