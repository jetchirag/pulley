from django.conf.urls import url
import views
from django.views.generic.base import RedirectView

urlpatterns = [
    url(r'^dashboard', views.dashboard, name='dashboard'),
    url(r'^$', RedirectView.as_view(url='dashboard', permanent=False)),
]