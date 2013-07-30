from django.shortcuts import render
from django.http import HttpResponseRedirect

from UserRegistration.models import UserTypeMasks
from CreateJob.forms import CreateJobForm
from CreateJob.models import Job


def createJob(request):
    if not request.user.is_authenticated():
        return HttpResponseRedirect('/register/login/')
    if request.user.is_authenticated() and request.user.user_type_mask != UserTypeMasks.Business:
        return HttpResponseRedirect('/profile/')
    
    if request.method == 'POST':
        form = CreateJobForm(request.POST)
        if form.is_valid():
            creator = request.user
            title = form.cleaned_data['title']
            duration = form.cleaned_data['duration']
            location = form.cleaned_data['location']
            is_paid = form.cleaned_data['is_paid']
            description = form.cleaned_data['description']
    
            # Create the job
            job = Job(creator=creator,
                title=title,
                duration=duration,
                location=location,
                is_paid=is_paid,
                description=description) 
            job.save()
            
            # Return to the job list
            return HttpResponseRedirect('/profile/')
    else:
        form = CreateJobForm()
        
    return render(request, 'CreateJob/create_job.html', {'form': form})

