from django.shortcuts import redirect
from teacher.models import Teacher
from django.views import View


class Add(View):
    def post(self,request):
        name = request.POST.get('name')
        role = request.POST.get('role')
        address = request.POST.get('address')
        phone = request.POST.get('phone')

        teach = Teacher(Name=name,Role=role,Address=address,Phone=phone)
        teach.save()
        return redirect('index')