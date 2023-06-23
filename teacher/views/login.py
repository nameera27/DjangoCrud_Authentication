from django.shortcuts import render, redirect
from django.contrib.auth import authenticate,login
from django.contrib import messages
from django.views import View

class LoginUser(View):
    def get(self,request):
        return render(request,'login.html')
    
    def post(self,request):
        loginusername=request.POST.get('loginusername')
        loginpassword=request.POST.get('loginpassword')

        user=authenticate(request,username=loginusername,password=loginpassword)
        if user is not None:
            login(request,user)
            return redirect('index')
        else:
            messages.warning(request, "Only Senior Teacher can access to the backends")