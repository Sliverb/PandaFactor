from django.conf.urls import patterns, include, url

from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    url(r'^', include('HomePage.urls', namespace='home')),
    url(r'^business/', include('RegisterBusiness.urls', namespace='business')),
    url(r'^register/', include('UserRegistration.urls', namespace='UserRegistration')),
    url(r'^admin/', include(admin.site.urls)),
)
