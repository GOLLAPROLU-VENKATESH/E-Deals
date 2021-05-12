from django.shortcuts import render
from store.models.estore import Estore
from store.models.category import Category
from store.models.product import Product

def dialydeals(request):
    category = Category.get_all_categories()
    product = Product.get_all_products()
    estore = Estore.get_all_estores()
    category_id = request.GET.get('category')
    estore_id= request.GET.get('estore_id')
    if category_id:
        if category_id:
            product = Product.get_all_categories_by_id(category_id)
        else:
            product = Product.get_all_products()
    if estore_id:
        if estore_id:
            product = Product.get_all_products_by_estore_id(estore_id)
        else:
            product = Product.get_all_products()
    data = {}
    data['product'] = product
    data['category'] = category
    data['estore'] = estore
    return render(request, 'dilalydeals.html', data)