from django.conf.urls import patterns, url
from HomePage import views

urlpatterns = patterns('',
    url(r'^$', views.index, name='index'),
    url(r'^terms/$', views.termsOfUse, name='terms'),
)
