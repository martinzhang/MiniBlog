from django.http import HttpResponse
from django.template import loader
from django.template.context import Context

def index(request):
    temp = loader.get_template('home.html')
    ctx = Context({})
    return HttpResponse(temp.render(ctx))

def blog_add(request):
    return HttpResponse("add ok")

def user_add(request):
        
    return HttpResponse("add ok")

def user_login(request):
    return HttpResponse("add ok")