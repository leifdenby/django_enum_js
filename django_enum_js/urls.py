from django.conf.urls import patterns, include, url

import views

urlpatterns = patterns('',
                       url(r'^enums_js/$', views.enums_js, name="enums_js"),
                       )
