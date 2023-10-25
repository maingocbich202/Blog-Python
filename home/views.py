from django.shortcuts import render
from .registration import Registration
from .login import LoginForm
from django.http import HttpResponseRedirect

# Create your views here.
def index(request): 
    return render(request,'pages/home.html')

def index1(request): 
    return render(request,'pages/news.html')

def index2(request): 
    return render(request,'pages/khoahoc.html')

def contact(request): 
    return render(request,'pages/contact.html')

def error_400(request, exception):
    context= {}
    return render(request,'', context)

def error_500(request):
    context= {}
    return render(request,'', context)
    
def register(request):
    form = Registration()
    if request.method == 'POST':
        form = Registration(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/')
    return render(request,'pages/registes.html', {'form':form})

def login(request):
    form = LoginForm()
    return render(request,'pages/login.html',)