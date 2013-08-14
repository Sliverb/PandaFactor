from django.shortcuts import render
from django.http import HttpResponseRedirect, HttpResponse

from Profile.forms import ContactInfoForm


# Create your views here.
def profileView(request):
    if request.user.is_authenticated():
        if request.user.is_student():
            return render(request, 'Profile/student_profile.html', {})
        if request.user.is_business():
            return render(request, 'Profile/business_profile.html', {})
        if request.user.is_school():
            return render(request, 'Profile/school_profile.html', {})
            
        # Fallback to a default profile for now
        return HttpResponse("Unsupported user type")
    else:
        return HttpResponseRedirect('/register/')


def contactInfo(request):
    if not request.user.is_authenticated():
        return HttpResponseRedirect('/register/login/')
    
    if request.method == 'POST':
        form = ContactInfoForm(request.POST)
        if form.is_valid():
            # Update the user object and save
            request.user.phone = form.cleaned_data['phone'];
            request.user.email = form.cleaned_data['email'];
            request.user.address = form.cleaned_data['address'];
            request.user.save(update_fields=['phone', 'email', 'address'])
            
            # Return to the user's profile
            return HttpResponseRedirect('/profile/')
    else:
        initial = {
            'email': request.user.email, 
            'phone': request.user.phone, 
            'address': request.user.address
        }
        form = ContactInfoForm(
            initial=initial
        )
        
    return render(request, 'Profile/contact_info.html', {'form': form})