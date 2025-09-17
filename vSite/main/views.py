from django.views.generic import TemplateView


class IndexView(TemplateView):
    template_name = 'main/main.html'

    def get_context_data(self, **kwargs):
        cotext = super().get_context_data(**kwargs)

        cotext["age"] = range(18, 80)
        return cotext
