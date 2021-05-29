from django.shortcuts import render, redirect
from store.models.estore import Estore
from store.models.category import Category
from store.models.product import Product
from store.models.contactus import ContactUs
from siguplogin.models import Customer


def index(request):
    category = Category.get_all_categories()
    product = Product.get_all_products()
    estore = Estore.get_all_estores()
    category_id = request.GET.get('category')
    estore_id = request.GET.get('estore_id')
    try:
        success = request.GET.get('success')
        login_success = request.GET.get('login_success')
    except:
        pass
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
    if success:
        data['success'] = success
    if login_success:
        data['login_success'] = login_success
    return render(request, 'index.html', data)


def aboutus(request):
    return render(request, 'aboutUs.html')


def contactus(request):
    return render(request, 'contactUs.html')


def postquery(request):
    if request.method == "POST":
        postData = request.POST
        user_name = postData.get('name')
        phone = postData.get('phonenumber')
        email = postData.get('email')
        query = postData.get('query')
        try:
            image_file = request.FILES['image'].file.read()
            problem = ContactUs(
                user_name=user_name,
                phone_number=phone,
                email=email,
                query=query,
                img=image_file
            )
        except:
            problem = ContactUs(
                user_name=user_name,
                phone_number=phone,
                email=email,
                query=query,
            )

        problem.register()
        return render(request, 'contactUs.html',{'submited': 1})


def profile(request):
    email = request.session['email']
    customer = Customer.get_customer_by_email(email)
    data={
       'customer':customer
    }
    return render(request,'profile.html',data)
