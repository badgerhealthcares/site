from django_distill import distill_path
from .views import SiteIndexView

def get_index():
    return None

urlpatterns = [
    distill_path('',
                 SiteIndexView.as_view(),
                 name='index',
                 distill_func=get_index,
                 distill_file='index.html'),

]

