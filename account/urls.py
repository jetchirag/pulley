from django.conf.urls import url
from django.contrib import admin
from django.contrib.auth import views as auth_views


urlpatterns = [
    url(r'^login/$', auth_views.LoginView.as_view(template_name='account/login.html',
                                                 redirect_authenticated_user=True), name='login'),
    url(r'^logout/$', auth_views.logout, name='logout'),
    url('change-password/', auth_views.PasswordChangeView.as_view(), name='changePassword'),
]
