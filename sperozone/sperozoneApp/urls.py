from django.conf.urls import patterns, url

from sperozoneApp import views

urlpatterns = patterns('',
    url(r'^(?P<pk>\d+)/$', views.controller, name='controller'),
    url(r'^(?P<pk>\d+)/$', views.controller, name='controller'),
    )