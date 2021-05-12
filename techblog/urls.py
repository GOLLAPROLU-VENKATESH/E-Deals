from django.urls import path, include
from .views import tblog,vblog
urlpatterns = [
path('techblog/',tblog,name='techblog'),
path('vblog/',vblog,name='vblog'),
]