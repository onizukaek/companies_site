from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^companies/$', views.companies_list),
    url(r'^companies/(?P<pk>[0-9]+)/$', views.company_detail),
]
