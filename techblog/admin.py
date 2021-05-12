from django.contrib import admin
from .models import Techblog
# Register your models here.
class AdminTechBlog(admin.ModelAdmin):
    list_display = ['heading']


admin.site.register(Techblog, AdminTechBlog)