from django.views.generic import TemplateView
from search.utils import cities, get_or_session


class IndexView(TemplateView):
    template_name = 'main/main.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["looking_for"] = get_or_session(self, 'looking_for')
        context["goal"] = get_or_session(self, 'goal')
        context["age_min"] = get_or_session(self, 'age_min')
        context["age_max"] = get_or_session(self, 'age_max')
        context["city"] = get_or_session(self, 'city')
        context["order"] = get_or_session(self, 'order')
        context["age"] = range(18, 81)
        context["cities"] = cities
        return context
