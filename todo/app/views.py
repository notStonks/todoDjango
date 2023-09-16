from django.views.generic.base import TemplateView
from .models import Task

from common.views import TitleMixin


class IndexView(TitleMixin, TemplateView):
    title = 'Джанго todo'
    template_name = 'app/index.html'