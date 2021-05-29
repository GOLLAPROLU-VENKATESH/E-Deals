from django.urls import path, include
from .views import index
from .views import dialydeals
from .views.index import aboutus,contactus,postquery,profile
from .views.graphs import graphs
urlpatterns = [
path('',index,name='home'),
path('DialyDeals/',dialydeals,name='dd'),
path('aboutus',aboutus),
path('contactus',contactus),
path('postquery',postquery),
path('profile',profile),
path('stats/',graphs)
]
