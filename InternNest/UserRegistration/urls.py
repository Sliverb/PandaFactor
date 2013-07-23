from django.conf.urls import patterns, url
from UserRegistration import views

urlpatterns = patterns('',
  url(r'^business/$', views.registerBusinessUser, name='registerBusinessUser'),
  url(r'^school/$', views.registerSchoolUser, name='registerSchoolUser'),
  url(r'^student/$', views.registerStudentUser, name='registerStudentUser'),
)
