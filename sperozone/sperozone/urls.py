from django.conf.urls import patterns, include, url

from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    url(r'^sperozoneApp/', include('sperozoneApp.urls', namespace="sperozoneApp")),
    url(r'^admin/', include(admin.site.urls)),
)