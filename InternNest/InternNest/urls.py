from django.conf.urls import patterns, include, url

from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    url(r'^', include('HomePage.urls', namespace='home')),
    url(r'^business/', include('RegisterBusiness.urls', namespace='business')),
    url(r'^profile/', include('Profile.urls', namespace='Profile')),
    url(r'^register/', include('UserRegistration.urls', namespace='UserRegistration')),
    url(r'^create/job/', include('CreateJob.urls', namespace='CreateJob')),
    url(r'^admin/', include(admin.site.urls)),
)
