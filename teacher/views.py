from django.shortcuts import render, redirect, HttpResponse
from teacher.models import Teacher
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.decorators import login_required
from django.contrib import messages

# Create your views here.
def home(request):
    teach = Teacher.objects.all()
    context = {
        'teach' : teach
    }
    return render(request,'home.html',context)

@login_required(login_url='loginuser')
def index(request):
    teach = Teacher.objects.all()
    context = {
        'teach' : teach
    }
    return render(request,'index.html',context)

def add(request):
    if request.method=='POST':
        name = request.POST.get('name')
        role = request.POST.get('role')
        address = request.POST.get('address')
        phone = request.POST.get('phone')

        teach = Teacher(Name=name,Role=role,Address=address,Phone=phone)
        teach.save()
        return redirect('index')

def edit(request):
    teach = Teacher.objects.all()
    context = {
        'teach' : teach
    }
    return render(request,'index.html',context)


def update(request, id):
    if request.method =='POST':
        name = request.POST.get('name')
        role = request.POST.get('role')
        address = request.POST.get('address')
        phone = request.POST.get('phone')

        teach = Teacher(id=id,Name=name,Role=role,Address=address,Phone=phone)
        teach.save()
        return redirect('index')
    
def delete(request,id):
    teach = Teacher.objects.filter(id=id)
    teach.delete()
    return redirect('index')


def loginuser(request):
    if request.method == 'POST':
        loginusername=request.POST.get('loginusername')
        loginpassword=request.POST.get('loginpassword')

        user=authenticate(request,username=loginusername,password=loginpassword)
        if user is not None:
            login(request,user)
            return redirect('index')
        else:
            messages.warning(request, "Only Senior Teacher can access to the backends")

    return render(request,'login.html')


def logoutuser(request):
    logout(request)
    return redirect('home')
