from django.http import HttpResponseRedirect, HttpResponse
from django.shortcuts import render, get_object_or_404
from django.core.urlresolvers import reverse
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, get_user_model, login, logout
from datetime import date

from UserRegistration.models import InternNestUserManager, UserTypeMasks
from UserRegistration.forms import LoginForm, RegisterUserForm


def loginUser(request):
    if request.user.is_authenticated():
        # If already logged in, redirect to the user's profile
        return HttpResponseRedirect('/profile/')
    
    # Object that gets populated and used for the call to render()
    context = {}
    
    # Handle the user submitting data
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            email = form.cleaned_data['email']
            password = form.cleaned_data['password']
            user = authenticate(email=email, password=password)
            if user is not None:
                if user.is_active:
                    # Success!
                    login(request, user)
                    return HttpResponseRedirect('/profile/')
                else:
                    context['login_error_message'] = 'account is no longer active'
            else:
                context['login_error_message'] = 'invalid login credentials'
        
        context['user_type'] = int(request.POST['user_type'])
        context['login_form'] = form
        context['register_form'] = RegisterUserForm()
        return render(request, 'UserRegistration/register.html', context)    
    
    # Handle the initial navigation to this address
    if request.method == '	GET':
        context['user_type'] = UserTypeMasks.Student
        context['login_form'] = LoginForm()
        context['register_form'] = RegisterUserForm()
        return render(request, 'UserRegistration/register.html', context) 
    
    # Go home if we get an invalid request type
    return HttpResponseRedirect('/')


def logoutUser(request):
    logout(request)
    return HttpResponseRedirect('/')
        

def registerUser(request):
    return registerUserShared(request, UserTypeMasks.Student)
    
    
def registerBusinessUser(request):
    return registerUserShared(request, UserTypeMasks.Business)

    
def registerSchoolUser(request):
    return registerUserShared(request, UserTypeMasks.School)


def registerStudentUser(request):
    return registerUserShared(request, UserTypeMasks.Student)
        
        
def registerUserShared(request, default_user_type):
    if request.user.is_authenticated():
        return HttpResponseRedirect('/profile/')
     
    # Object that gets populated and used for the call to render()
    context = {}
     
    if request.method == 'POST':
        form = RegisterUserForm(request.POST)
        if form.is_valid():
            # Success! Creates and save the new user
            first_name = form.cleaned_data['first_name']
            last_name = form.cleaned_data['last_name']
            email = form.cleaned_data['email']
            password = form.cleaned_data['password']
            user_type = int(request.POST['user_type'])

            get_user_model().objects.create_user(
                first_name = first_name,
                last_name = last_name,
                email = email,
                date_of_birth = date.today(),
                user_type_mask = user_type,
                password = password,
            )
            user = authenticate(username=email, password=password) 
            login(request, user)
            return HttpResponseRedirect('/profile/')
            
        context['login_error_message'] = 'some invalid data login credentials'
        context['user_type'] = int(request.POST['user_type'])
        context['login_form'] = LoginForm()
        context['register_form'] = form
        return render(request, 'UserRegistration/register.html', context)
        
    # Handle the initial navigation to this address
    if request.method == 'GET':
        context['user_type'] = default_user_type
        context['login_form'] = LoginForm()
        context['register_form'] = RegisterUserForm()
        return render(request, 'UserRegistration/register.html', context) 
        
    # Go home if we get an invalid request type
    return HttpResponseRedirect('/')


   
