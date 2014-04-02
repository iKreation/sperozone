from django.conf.urls import patterns, url

from sperozoneApp import views

urlpatterns = patterns('',
    url(r'^ocorrencias/(?P<pk>\d+)/$', views.controller, name='controller'),
    url(r'^ocorrencias/',views.controller, name='controller'),
)