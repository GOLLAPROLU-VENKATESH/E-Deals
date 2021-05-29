from django.contrib import admin

from .models import Customer


class AdminCustomer(admin.ModelAdmin):
    list_display = ['user_name', 'phone_number', 'email']




admin.site.register(Customer, AdminCustomer)

