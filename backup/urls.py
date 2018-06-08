from django.conf.urls import url
import views
from django.views.generic.base import RedirectView

urlpatterns = [
    url(r'^$', RedirectView.as_view(url='/base/dashboard', permanent=False)),
    
    url(r'^jobs', views.jobs, name='jobs'),
    url(r'^addJob', views.addJob, name='addJob'),
    
    # POST URLS
    url(r'^submitAddJob', views.submitAddJob),
]