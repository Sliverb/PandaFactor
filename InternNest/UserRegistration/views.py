from django.http import HttpResponseRedirect, HttpResponse
from django.shortcuts import render, get_object_or_404
from django.core.urlresolvers import reverse
from django.contrib.auth.models import User
from django.contrib.auth import get_user_model
from datetime import date

from UserRegistration.models import InternNestUserManager


def registerBusinessUser(request):
    context = {}
    return render(request, 'UserRegistration/register.html', context)

def createBusinessUser(request):
    try:
        firstName = request.POST['firstName']
        if not firstName:
            raise KeyError
    except (KeyError):
        context = {'error_message': 'you didn\'t specify a first name'}
        return render(request, 'UserRegistration/register.html', context)

    try:
        lastName = request.POST['lastName']
        if not lastName:
            raise KeyError
    except (KeyError):
        context = {'error_message': 'you didn\'t specify a last name'}
        return render(request, 'UserRegistration/register.html', context)    
        
    try:
        email = request.POST['email']
        if not email:
            raise KeyError
    except (KeyError):
        context = {'error_message': 'you didn\'t specify an email'}
        return render(request, 'UserRegistration/register.html', context)
        
    try:
        email2 = request.POST['email2']
        if not email2:
            raise KeyError
    except (KeyError):
        context = {'error_message': 'you didn\'t re-enter your email'}
        return render(request, 'UserRegistration/register.html', context)
  
    if (email.lower() != email2.lower()):
        context = {'error_message': 'the entered emails don\'t match'}
        return render(request, 'UserRegistration/register.html', context)

    try:
        password = request.POST['password']
        if not password:
            raise KeyError
    except (KeyError):
        context = {'error_message': 'you didn\'t specify a password'}
        return render(request, 'UserRegistration/register.html', context)
        
    try:
        password2 = request.POST['password2']
        if not password2:
            raise KeyError
    except (KeyError):
        context = {'error_message': 'you didn\'t re-enter your password'}
        return render(request, 'UserRegistration/register.html', context)
        
    if (password != password2):
        context = {'error_message': 'the entered passwords don\'t match'}
        return render(request, 'RegisterBusiness/register.html', context)  
    
    get_user_model().objects.create_user(
        first_name = firstName,
        last_name = lastName,
        email = email,
        date_of_birth = date.today(),
        user_type_mask = 1,
        password = password,
    )
    
    # Return an HttpResponseRedirect after successfully dealing
    # with POST data. This prevents data from being posted twice if a
    # user hits the Back button.
    return HttpResponseRedirect('/admin/')
    
    
'''
def registerSchoolUser(request):
    return HttpResponse("Register school needs implementing.")


def registerStudentUser(request):
    return HttpResponse("Register Student needs implementing.")
'''