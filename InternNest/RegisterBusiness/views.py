from django.http import HttpResponseRedirect
from django.shortcuts import render, get_object_or_404
from django.core.urlresolvers import reverse

from RegisterBusiness.models import Business

def list(request):
    # Displays a list of all Businesses
    businesses_list = Business.objects.all()
    context = {'businesses_list': businesses_list}
    return render(request, 'RegisterBusiness/index.html', context)
    
def register(request):
    context = {}
    return render(request, 'RegisterBusiness/register.html', context)
    
def create(request):
    try:
        b_name = request.POST['name']
        if not b_name:
            raise KeyError
    except (KeyError):
        context = {'error_message': 'you didn\'t specify a name'}
        return render(request, 'RegisterBusiness/register.html', context)
    try:
        b_email = request.POST['email']
        if not b_email:
            raise KeyError
    except (KeyError):
        context = {'error_message': 'you didn\'t specify an email'}
        return render(request, 'RegisterBusiness/register.html', context)
        
    business = Business(name=b_name, email = b_email) 
    business.save()
    
    # Return an HttpResponseRedirect after successfully dealing
    # with POST data. This prevents data from being posted twice if a
    # user hits the Back button.
    return HttpResponseRedirect(reverse('business:list'))


def view(request, business_id):
    business = get_object_or_404(Business, pk=business_id)
    context = {
      'name': business.name,
      'email': business.email,
    }
    return render(request, 'RegisterBusiness/view.html', context)
    
