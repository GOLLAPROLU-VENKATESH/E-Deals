from django.contrib import admin
from .models.product import Product
from .models.estore import Estore
from .models.category import Category
# Register your models here.


class AdminProduct(admin.ModelAdmin):
    list_display = ['name', 'category', 'estore', 'rating',
                    'selling_price', 'status', 'uploaded_time']


class AdminCategory(admin.ModelAdmin):
    list_display = ['name']


class AdminEstore(admin.ModelAdmin):
    list_display = ['name']


admin.site.register(Product, AdminProduct)
admin.site.register(Category, AdminCategory)
admin.site.register(Estore, AdminEstore)

