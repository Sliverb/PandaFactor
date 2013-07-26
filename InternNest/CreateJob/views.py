from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from UserRegistration.models import UserTypeMasks


def createJob(request):
    # If not a business, send them to the home page
    if not (request.user.is_authenticated() and request.user.user_type_mask == UserTypeMasks.Business):
        return HttpResponseRedirect('/')
        
    return render(request, 'CreateJob/create_job.html', {})