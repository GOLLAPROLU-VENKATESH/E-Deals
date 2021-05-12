from django.shortcuts import render,redirect
from .forms import AddLinkForm
from .models import Link
from django.views import View
from django.views.generic import DeleteView
from django.urls import reverse_lazy
from .utils import get_link_data
from django.core.mail import EmailMessage
from django.conf import settings

class AddProduct(View):
    def post(self, request):
        postData = request.POST
        url = postData.get('url')
        name, current_price ,erro = get_link_data(url)
        try:
            c=0
            customer=request.session['email']
        except:
            c=1
            erro=1
        target_price=postData.get('tp')
        try:
            tp=0
            target_price=float(target_price)
        except:
            tp=1
            erro = 1
        nemail=False
        qs = Link.objects.filter(customer=customer)
        items_no = qs.count()
        if items_no > 0:
            discount_list = []
            for item in qs:
                if item.target_price > item.current_price:
                    if nemail:
                        pass
                    else:
                        # sendig email
                        email = EmailMessage(
                            'Price Drop‼‼‼‼〽',
                            f'Hello {customer.user_name} ,'
                            f'Price reduced on product {item.name}'
                            f'Target price :{item.target_price}'
                            f'Current Price :{item.current_price}'
                            f'Buy Know>>>>>> {item.url}'
                            f'Ready to track othere one!!!!',
                            settings.EMAIL_HOST_USER,
                            [nemail],
                        )
                        email.fail_silently = False
                        email.send()
                    discount_list.append(item)
                no_discounted = len(discount_list)
        if erro==0:
            if current_price!=target_price:
                price_diff=current_price-target_price
                price_diff=round(price_diff, 2)
            else:
                price_diff = 0
        else:
            if tp==1:
                error="Enter Correct Product Details"
            elif c==1:
                error="Login To track a product"
            else:
                error="Invalid Url or check if the product is in Offer or Not in Respective Ecommers website"
            context = {
                'qs': qs,
                'items_no': items_no,
                'no_discounted': no_discounted,
                'error': error,
            }
            return render(request, 'links/pricetracker.html', context)

        product=Link(
            name=name,
            url=url,
            current_price=current_price,
            target_price=target_price,
            price_diff=price_diff,
            nemail=nemail,
            customer=customer
        )
        product.register()

        return redirect('pt')





def price_tracker(request):
    # qs = Link.objects.all()
    # for link in qs:
    #     link.save()
    no_discounted = 0
    error = None
    form = AddLinkForm(request.POST or None)

    if request.method == 'POST':
        try:
            if form.is_valid():
                form.save()
        except AttributeError:
            error = "Opps No product found Check link "
        except:
            error = "Check the Url "
    customer = request.session['email']
    form = AddLinkForm()
    qs = Link.objects.filter(customer=customer)
    items_no = qs.count()
    if items_no > 0:
        discount_list = []
        for item in qs:
            if item.target_price > item.current_price:
                if item.nemail:
                    pass
                else:
                    email = EmailMessage(
                        'Price Drop‼‼‼‼〽',
                        f'Hello {customer} ,'
                        f'Price reduced on product {item.name}'
                        f'Target price :{item.target_price}'
                        f'Current Price :{item.current_price}'
                        f'Buy Know>>>>>> {item.url} '
                        f' Ready to track othere one!!!!',
                        settings.EMAIL_HOST_USER,
                        [customer],
                    )
                    email.fail_silently = False
                    email.send()
                    up=Link.objects.filter(name=item.name)
                    for o in up:
                        o.nemail=True
                        o.save()
                discount_list.append(item)
            no_discounted = len(discount_list)
    context = {
        'qs': qs,
        'items_no': items_no,
        'no_discounted': no_discounted,
        'form': form,
        'error': error,
    }

    return render(request, 'links/pricetracker.html', context)


class LinkDeleteView(DeleteView):
    model = Link
    template_name = 'links/confirm_del.html'
    success_url = reverse_lazy('pt')


def update_price(request):
    qs = Link.objects.all()
    for link in qs:
        link.save()
    return redirect('pt')

