from django.urls import path, include
from .views import index
from .views import dialydeals
urlpatterns = [
path('',index,name='home'),
path('DialyDeals/',dialydeals,name='dd')
]
