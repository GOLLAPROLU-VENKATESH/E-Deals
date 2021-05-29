from django.urls import path
from .views import compare,getdetails
urlpatterns = [
path('compare',compare),
path('getdetails',getdetails)

]