from django.http import HttpResponseRedirect, HttpResponse
from django.shortcuts import render, get_object_or_404
from django.core.urlresolvers import reverse
from django.contrib.auth.models import User
from django.contrib.auth import get_user_model
from datetime import date

from UserRegistration.models import InternNestUserManager, UserTypeMasks
 

def registerBusinessUser(request):
    return registerUserShared(request, 'UserRegistration/register.html', UserTypeMasks.Business)

    
def registerSchoolUser(request):
    return registerUserShared(request, 'UserRegistration/register.html', UserTypeMasks.School)


def registerStudentUser(request):
    return registerUserShared(request, 'UserRegistration/register.html', UserTypeMasks.Student)
    
    
def registerUserShared(request, url, userType):
    if (request.method == 'POST'):
        try:
            firstName = request.POST['firstName']
            if not firstName:
                raise KeyError
        except (KeyError):
            context = {
                'error_message': 'you didn\'t specify a first name',
                'current_url': request.path,
            }
            return render(request, url, context)

        try:
            lastName = request.POST['lastName']
            if not lastName:
                raise KeyError
        except (KeyError):
            context = {
                'error_message': 'you didn\'t specify a last name',
                'current_url': request.path,
            }
            return render(request, url, context)    
            
        try:
            email = request.POST['email']
            if not email:
                raise KeyError
            email = email.lower()
        except (KeyError):
            context = {
                'error_message': 'you didn\'t specify an email',
                'current_url': request.path,
            }
            return render(request, url, context)
            
        try:
            email2 = request.POST['email2']
            if not email2:
                raise KeyError
            email2 = email2.lower()
        except (KeyError):
            context = {
                'error_message': 'you didn\'t re-enter your email',
                'current_url': request.path,
            }
            return render(request, url, context)
      
        if (email != email2):
            context = {
                'error_message': 'the entered emails don\'t match',
                'current_url': request.path,
            }
            return render(request, url, context)

        try:
            password = request.POST['password']
            if not password:
                raise KeyError
        except (KeyError):
            context = {
                'error_message': 'you didn\'t specify a password',
                'current_url': request.path,
            }
            return render(request, url, context)
            
        try:
            password2 = request.POST['password2']
            if not password2:
                raise KeyError
        except (KeyError):
            context = {
                'error_message': 'you didn\'t re-enter your password',
                'current_url': request.path,
            }
            return render(request, url, context)
            
        if (password != password2):
            context = {
                'error_message': 'the entered passwords don\'t match',
                'current_url': request.path,
            }
            return render(request, url, context)  
        
        # Check if the user already exists
        alreadyExists = get_user_model().objects.filter(email=email).count()
        if (alreadyExists):
            context = {
                'error_message': 'that email is already registered to a user',
                'current_url': request.path,
            }
            return render(request, url, context)  
        
        # Creates and saves the new user object
        get_user_model().objects.create_user(
            first_name = firstName,
            last_name = lastName,
            email = email,
            date_of_birth = date.today(),
            user_type_mask = userType,
            password = password,
        )
        
        # Return an HttpResponseRedirect after successfully dealing
        # with POST data. This prevents data from being posted twice if a
        # user hits the Back button.
        return HttpResponseRedirect('/admin/')
    else:
        context = {'current_url': request.path}
        return render(request, url, context)
