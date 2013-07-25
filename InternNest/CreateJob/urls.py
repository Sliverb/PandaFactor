from django.conf.urls import patterns, url
from CreateJob import views

urlpatterns = patterns('',
  url(r'^$', views.createJob, name='createJob'),
)
