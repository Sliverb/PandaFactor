from django.conf.urls import patterns, url
from RegisterBusiness import views

urlpatterns = patterns('',
    url(r'^$', views.list, name='list'),
    url(r'^register/$', views.register, name='register'),
    url(r'^create/$', views.create, name='create'),
    url(r'^view/(?P<business_id>\d+)/$', views.view, name='view'),
)
