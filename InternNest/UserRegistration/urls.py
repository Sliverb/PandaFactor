from django.conf.urls import patterns, url
from UserRegistration import views

urlpatterns = patterns('',
  url(r'^$', views.registerUser, name='registerUser'),
  url(r'^login/$', views.loginUser, name='loginUser'),
  url(r'^logout/$', views.logoutUser, name='logoutUser'),
  url(r'^business/$', views.registerBusinessUser, name='registerBusinessUser'),
  url(r'^school/$', views.registerSchoolUser, name='registerSchoolUser'),
  url(r'^student/$', views.registerStudentUser, name='registerStudentUser'),
)
