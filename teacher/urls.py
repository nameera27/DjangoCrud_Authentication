from django.urls import path
from teacher import views

urlpatterns = [
    path('',views.home,name='home'),
    path('index',views.index,name='index'),
    path('add',views.add,name='add'),
    path('edit',views.edit,name='edit'),
    path('update/<str:id>',views.update,name='update'),
    path('delete/<int:id>',views.delete,name='delete'),
    path('loginuser',views.loginuser,name='loginuser'),
    path('logoutuser',views.logoutuser,name='logoutuser'),
]