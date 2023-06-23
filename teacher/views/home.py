from django.shortcuts import render, redirect
from teacher.models import Teacher
from django.contrib.auth import logout
from django.contrib.auth.decorators import login_required

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


def edit(request):
    teach = Teacher.objects.all()
    context = {
        'teach' : teach
    }
    return render(request,'index.html',context)


def delete(request,id):
    teach = Teacher.objects.filter(id=id)
    teach.delete()
    return redirect('index')


def logoutuser(request):
    logout(request)
    return redirect('home')