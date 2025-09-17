from django.views.generic import TemplateView
from search.utils import cities


class IndexView(TemplateView):
    template_name = 'main/main.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["age"] = range(18, 80)
        context["cities"] = cities
        return context
