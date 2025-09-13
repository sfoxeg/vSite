from django.views.generic import TemplateView
from utils import name, names, cities


class IndexView(TemplateView):
    template_name = 'main/main.html'

    def get_context_data(self, **kwargs):
        cotext = super().get_context_data(**kwargs)
        cotext["name"] = name(self.request)
        cotext["city"] = cities
        cotext["names"] = names
        cotext["age"] = range(18, 80)
        return cotext
