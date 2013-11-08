__author__ = 'droghetti'
from django.views.generic import TemplateView, View
from mixin import LoginRequiredMixin

class MainView(LoginRequiredMixin, TemplateView):
    template_name = 'portfolio-item.html'

    def get_context_data(self, **kwargs):
        context = super(MainView, self).get_context_data()
        return context