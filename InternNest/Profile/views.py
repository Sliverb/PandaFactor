from django.shortcuts import render
from django.http import HttpResponseRedirect
from UserRegistration.models import UserTypeMasks

# Create your views here.
def profileView(request):
    if request.user.is_authenticated():
        if request.user.user_type_mask == UserTypeMasks.Student:
            return render(request, 'Profile/student_profile.html', {})
        if request.user.user_type_mask == UserTypeMasks.Business:
            return render(request, 'Profile/business_profile.html', {})
        if request.user.user_type_mask == UserTypeMasks.School:
            return render(request, 'Profile/school_profile.html', {})
            
        # Fallback to a default profile for now
        return HttpResponse("Unsupported user type")
    else:
        return HttpResponseRedirect('/register/')