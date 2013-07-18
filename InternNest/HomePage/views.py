from django.template.loader import get_template
from django.template import Context
from django.http import HttpResponse

def index(request):    
    t = get_template('base.html')
    html = t.render(Context({'test_message': 'This is a test message'}))
    return HttpResponse(html)