from django.views.generic.base import TemplateView

# Create your views here.
class SiteIndexView(TemplateView):
    template_name = 'site_index.html'
