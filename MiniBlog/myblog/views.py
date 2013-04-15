from django.core.context_processors import csrf
from django.core.urlresolvers import reverse
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render_to_response, get_object_or_404
from django.template import loader
from django.template.context import Context
from myblog.modelforms import UserForm
from myblog.models import User

def index(request):
    temp = loader.get_template('home.html')
    ctx = Context({})
    return HttpResponse(temp.render(ctx))

def blog_add(request):
    return HttpResponse("add ok")

def user_add(request):
    userForm = UserForm()
    if request.method == 'POST' :
        p = request.POST
        u = UserForm(p)
        if u.is_valid() : 
            au = u.save()
            return HttpResponseRedirect(reverse(user_detail, args=[au.id]))
    #temp = loader.get_template("user/add.html");
    ctx = {'user':userForm}
    ctx.update(csrf(request))
    return render_to_response('user/add.html', ctx)

def user_detail(request, pk):
    #u = User.objects.get(pk=pk);
    u = get_object_or_404(User, pk = pk)
    return render_to_response('user/detail.html', {'user':u})

def user_list(request):
    u = User.objects.all();
    return render_to_response('user/list.html', {'users':u})

def user_login(request):
    uf = UserForm()
    if request.method == 'POST':
        uf = UserForm(request.POST)
        if uf.is_valid():
            u = User.objects.filter(login_id = uf.cleaned_data['login_id']).get()
            #u = uf.cleaned_data['login_id']
            return HttpResponse("login ok" + str(u))
            
    ctx = {'user':uf}
    ctx.update(csrf(request))
    return render_to_response('user/login.html',  ctx)