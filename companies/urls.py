from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.IndexView.as_view(), name='index'),
    url(r'^update/(?P<pk>\d+)/$', views.CompanyUpdateView.as_view(), name='update'),
    url(r'^delete/(?P<pk>\d+)/$', views.delete, name='delete'),
    url(r'^add/$', views.add, name='add'),
    url(r'^save/$', views.save, name='save'),
    # url(r'^welcome/', views.welcome, name='welcome'),
    # url(r'^signup/', views.signup, name='signup'),
    # url(r'^logout/', views.LogoutView.as_view(), name='logout'),
]
