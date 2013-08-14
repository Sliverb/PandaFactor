from django.shortcuts import render

def index(request):    
    context = {
        'test_message': "Content from \\InternNest\\HomePage\\views.py but used in \\InternNest\\templates\\base.html",
        'context_message': "This string is used in \\InternNest\\HomePage\\templates\\HomePage\\body.html",
    }
    return render(request, 'HomePage/body.html', context)
    
def termsOfUse(request):
    context = {}
    return render(request, 'HomePage/terms_of_use.html', context)