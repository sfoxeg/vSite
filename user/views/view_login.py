from django.contrib.auth.views import LoginView
from django.urls import reverse_lazy
from user.forms import UserLoginForm


class UserLoginView(LoginView):
    template_name = 'user/login.html'
    form_class = UserLoginForm
    success_url = reverse_lazy('user:profile')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["title"] = 'Вход'
        return context
