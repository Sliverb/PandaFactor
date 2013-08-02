from django.conf.urls import patterns, url
from Profile import views

urlpatterns = patterns('',
    url(r'^$', views.profileView, name='profileView'),
    url(r'^contactinfo/$', views.contactInfo, name='contactInfo'),
)
