from django.urls import reverse_lazy
from django.views.generic import CreateView
from user.forms import UserRegistrationForm


class UserRegistrationView(CreateView):
    template_name = 'user/registration.html'
    form_class = UserRegistrationForm
    success_url = reverse_lazy('user:login')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["title"] = 'Регистрация'
        return context
