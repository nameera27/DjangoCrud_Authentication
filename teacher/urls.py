from django.urls import path
from .views.login import LoginUser
from .views.update import Update
from .views.add import Add
from .views import home

urlpatterns = [
    path('',home.home,name='home'),
    path('index',home.index,name='index'),
    path('add',Add.as_view(),name='add'),
    path('edit',home.edit,name='edit'),
    path('update/<str:id>',Update.as_view(),name='update'),
    path('delete/<int:id>',home.delete,name='delete'),
    path('loginuser',LoginUser.as_view(),name='loginuser'),
    path('logoutuser',home.logoutuser,name='logoutuser'),
    
]