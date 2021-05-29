from django.shortcuts import render, redirect
from siguplogin.models import Customer
from django.contrib.auth.hashers import make_password
from django.views import View
from django.core.mail import EmailMessage
from django.conf import settings
from django.template.loader import render_to_string, get_template

class Signup(View):
    def validatecustomer(self, customer):
        error_message = None
        if not customer.first_name:
            error_message = "First Name Requried !!"
        elif len(customer.first_name) < 3:
            error_message = "First Name must be atleast 3  character long"
        elif not customer.last_name:
            error_message = "Last Name Requried !!"
        elif len(customer.last_name) < 3:
            error_message = "Last Name must be atleast 3  character long"
        elif not customer.user_name:
            error_message = "User Name Requried !!"
        elif len(customer.user_name) < 3:
            error_message = "User Name must be atleast 3  character long"
        elif not customer.phone_number:
            error_message = "Phone number Requried !!"
        elif len(customer.phone_number) < 10:
            error_message = "Phone number must be 10 (+91)"
        elif not customer.email:
            error_message = "Email Requried !!"
        elif len(customer.last_name) < 5:
            error_message = "Email must be atleast 20  character long"
        elif not customer.password:
            error_message = "Password Requried !!"
        elif len(customer.password) < 8:
            error_message = "Password must be 8 characters"
        elif customer.isUserExists():
            error_message = "UserName Already Registered"
        elif customer.isEmailExists():
            error_message = "Email Already Registered"
        elif customer.isPhoneExists():
            error_message = "PhoneNumber Already Registered"
        return error_message

    def get(self, request):
        return render(request, 'index.html')

    def post(self, request):
        postData = request.POST
        first_name = postData.get('FirstName')
        last_name = postData.get('LastName')
        user_name = postData.get('UserName')
        email = postData.get('Email')
        phone_number = postData.get('PhoneNumber')
        password = postData.get('Password')
        customer = Customer(first_name=first_name,
                            last_name=last_name,
                            user_name=user_name,
                            email=email,
                            phone_number=phone_number,
                            password=password,
                            )
        value = {
            'first_name': first_name,
            'last_name': last_name,
            'user_name': user_name,
            'email': email,
            'phone_number': phone_number,
        }
        error_message = self.validatecustomer(customer)
        if not error_message:
            customer.password = make_password(customer.password)
            customer.register()
            #sendig email
            ctx = {
                'user_name': user_name
            }
            message = get_template('signupmail.html').render(ctx)
            email=EmailMessage(
                'Welcome to E-Deals! 😀 ',
                message,
                settings.EMAIL_HOST_USER,
                [email],
            )
            email.content_subtype = "html"
            email.fail_silently=False
            email.send()
            return redirect('/?success=1')
        else:
            data = {
                'error': error_message,
                'value': value
            }
            return render(request, 'index.html', data)


from django.shortcuts import render, redirect
from siguplogin.models import Customer
from django.contrib.auth.hashers import check_password
from django.views import View


class Login(View):
    def get(self, request):
        return render(request, 'index.html')

    def post(self, request):
        email = request.POST.get("lemail")
        password = request.POST.get("lpassword")
        customer = Customer.get_customer_by_email(email)
        error_message = None
        if customer:
            flag = check_password(password, customer.password)
            if flag:
                request.session['customer_id']=customer.id
                request.session['email']=email
                request.session['name']=customer.user_name
                return redirect('/?login_success=1')
            else:
                error_message = "Email Or Password Incorrect!!"
        else:
            error_message = "Email Or Password Incorrect!!"
        return render(request, 'index.html', {'error': error_message})

def logout(request):
    request.session.clear()
    return redirect('home')