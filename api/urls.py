from django.conf.urls import url, include
from . import views

urlpatterns = [
    url(r'^users/$', views.UserList.as_view()),
    url(r'^users/(?P<pk>[0-9]+)/$', views.UserDetail.as_view()),
    url(r'^companies/$', views.CompaniesList.as_view()),
    url(r'^companies/(?P<pk>[0-9]+)/$', views.CompanyDetail.as_view()),
]

urlpatterns += [
    url(r'^auth/', include('rest_framework.urls', namespace='rest_framework')),
]
