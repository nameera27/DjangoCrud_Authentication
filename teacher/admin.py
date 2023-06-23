from django.contrib import admin
from .models import *


class AdminProduct(admin.ModelAdmin):
    list_display = ['Name', 'Role']


# Register your models here.
admin.site.register(Teacher, AdminProduct)