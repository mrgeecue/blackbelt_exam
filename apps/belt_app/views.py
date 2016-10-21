from django.shortcuts import render, redirect

# from .models import
# Create your views here.

def index(request):
    name = 'name %s' %(request.user)
    alias = 'alias'
    email = 'email'
    password = 'password'
    dob = 'dob'
    context = {
        "name" : name, "alias": alias, "email": email, "password": password, "dob": dob
    }

    if request.method == "POST":
        print request.POST

    return render(request, 'belt_app/index.html', context=context)

def pokes(request):
    return render(request,'belt_app/pokes.html')
