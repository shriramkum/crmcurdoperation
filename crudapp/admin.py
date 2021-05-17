from django.contrib import admin

from .models import Customer
class Customeradmin(admin.ModelAdmin):
    list_display = ['id','first_name','last_name','email','mobile_number','data_store']
admin.site.register(Customer,Customeradmin)