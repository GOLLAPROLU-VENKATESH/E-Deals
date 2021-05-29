from django.urls import path
from .views import price_tracker,update_price,LinkDeleteView,AddProduct,targetprices

urlpatterns = [
path('price_tracker', price_tracker,name='pt'),
path('update/', update_price, name='update'),
path('delete/<pk>/', LinkDeleteView.as_view(), name='delete'),
path('addproduct',AddProduct.as_view(),name='ap'),
path('suggestedprices',targetprices,name='sp')
]