from django.http import HttpResponseRedirect, HttpResponse
from django.shortcuts import render, get_object_or_404
from django.core.urlresolvers import reverse
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, get_user_model, login, logout
from datetime import date

from UserRegistration.models import InternNestUserManager, UserTypeMasks


def loginUser(request):
    if request.user.is_authenticated():
        # If already logged in, redirect to the user's profile
        return HttpResponseRedirect('/profile/')
    else:
        if (request.method == 'POST'):
            context = {
                'user_type': request.POST['userType']
            }
            try:
                email = request.POST['email']
                if not email:
                    raise KeyError
                context['email'] = email
                email = email.lower()
            except (KeyError):
                context['login_error_message'] = 'you didn\'t specify an email'
                return registerUserError(request, context)
                
            try:
                password = request.POST['password']
                if not password:
                    raise KeyError
            except (KeyError):
                context['login_error_message'] = 'you didn\'t specify a password'
                return registerUserError(request, context)
        
            user = authenticate(email=email, password=password)
            if (user is not None) and (user.is_active):
                login(request, user)
                return HttpResponseRedirect('/profile/')
            else:
                context['login_error_message'] = 'invalid credentials'
                return registerUserError(request, context)
        else:
            return registerUser(request)


def logoutUser(request):
    logout(request)
    return HttpResponseRedirect('/')
        

def registerUser(request):
    if request.user.is_authenticated():
        return HttpResponseRedirect('/profile/')
        
    if (request.method == 'POST'):
        return registerUserShared(request, 'UserRegistration/register.html', request.POST['userType'])
    else:
        return render(request, 'UserRegistration/register.html', {'user_type': UserTypeMasks.Student})

        
def registerUserError(request, context):
    return render(request, 'UserRegistration/register.html', context)

    
def registerBusinessUser(request):
    if request.user.is_authenticated():
        return HttpResponseRedirect('/profile/')
    return registerUserShared(request, 'UserRegistration/register.html', UserTypeMasks.Business)

    
def registerSchoolUser(request):
    if request.user.is_authenticated():
        return HttpResponseRedirect('/profile/')
    return registerUserShared(request, 'UserRegistration/register.html', UserTypeMasks.School)


def registerStudentUser(request):
    if request.user.is_authenticated():
        return HttpResponseRedirect('/profile/')
    return registerUserShared(request, 'UserRegistration/register.html', UserTypeMasks.Student)
    
    
def registerUserShared(request, url, userType):
    if (request.method == 'POST'):
        context = {
            'user_type': userType,
        }
        
        try:
            firstName = request.POST['firstName']
            if not firstName:
                raise KeyError
            context['first_name'] = firstName
        except (KeyError):
            context['register_error_message'] = 'you didn\'t specify a first name'
            return registerUserError(request, context)

        try:
            lastName = request.POST['lastName']
            if not lastName:
                raise KeyError
            context['last_name'] = lastName
        except (KeyError):
            context['register_error_message'] = 'you didn\'t specify a last name'
            return registerUserError(request, context)
            
        try:
            email = request.POST['email']
            if not email:
                raise KeyError
            context['email'] = email
            email = email.lower()
        except (KeyError):
            context['register_error_message'] = 'you didn\'t specify an email'
            return registerUserError(request, context)
            
        try:
            email2 = request.POST['email2']
            if not email2:
                raise KeyError
            context['email2'] = email2
            email2 = email2.lower()
        except (KeyError):
            context['register_error_message'] = 'you didn\'t re-enter your email'
            return registerUserError(request, context)
      
        if (email != email2):
            context['register_error_message'] = 'the entered emails don\'t match'
            return registerUserError(request, context)

        try:
            password = request.POST['password']
            if not password:
                raise KeyError
        except (KeyError):
            context['register_error_message'] = 'you didn\'t specify a password'
            return registerUserError(request, context)
            
        try:
            password2 = request.POST['password2']
            if not password2:
                raise KeyError
        except (KeyError):
            context['register_error_message'] = 'you didn\'t re-enter your password'
            return registerUserError(request, context)
            
        if (password != password2):
            context['register_error_message'] = 'the entered passwords don\'t match'
            return registerUserError(request, context)            
        
        # Check if the user already exists
        alreadyExists = get_user_model().objects.filter(email=email).count()
        if (alreadyExists):
            context['register_error_message'] = 'that email is already registered to a user'
            return registerUserError(request, context)     
        
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
        return HttpResponseRedirect('/profile/')
    else:
        return render(request, 'UserRegistration/register.html', {'user_type': userType})