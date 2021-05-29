from django.shortcuts import render
from .utils import get_link_data


# Create your views here.
def compare(request):
    return render(request, 'compare.html')


def getdetails(request):
    postData = request.POST
    url = postData.get('aurl')
    url2 = postData.get('furl')
    name, price, fls = get_link_data(url)
    name2, price2, fls2 = get_link_data(url2)
    # print(fls)
    # print(fls2)
    ls = []
    ls2 = []
    try:
        if fls['Whats in the box'] and fls2["In The Box"]:
            ls.append("What is in the box" +"          :     " + fls["Whats in the box"])
            ls2.append("What is in the box" + "          :     " + fls2["In The Box"])
    except:
        pass
    try:
        if fls['Product Dimensions'] and (fls2['Width'] and fls2['Height'] and fls2['Depth'] and fls2['Weight']):
            ls.append('Product Dimensions(l x b x h ; w)' + "          :     " + fls['Product Dimensions'])
            ls2.append('Product Dimensions(l x b x h ; w)' + "          :     " + fls2['Width'] + " x " + fls2['Height'] + " x " + fls2['Depth'] + " ; " + fls2['Weight'])
    except:
        pass
    try:
        if fls["OS"] and fls2["Operating System"]:
            ls.append("Operating System" + "          :     " + fls["OS"])
            ls2.append("Operating System" +"          :     " + fls2["Operating System"])
    except:
        pass
    try:
        if fls['RAM'] and fls2['RAM']:
            ls.append("RAM" +"          :     "+ fls['RAM'])
            ls2.append("RAM" +"          :     " + fls2["RAM"])
    except:
        pass
    try:
        if fls['Colour'] and fls2['Color']:
            ls.append("COLOUR" + "          :     "+ fls['Colour'])
            ls2.append("COLOUR" +"          :     "+ fls2["Color"])
    except:
        pass
    try:
        if fls['Battery Power Rating'] and fls2['Battery Capacity']:
            ls.append("Battery Power Rating" + "          :     " + fls['Battery Power Rating'])
            ls2.append("Battery Power Rating" +"          :     "+ fls2["Battery Capacity"])
    except:
        pass
    try:
        if fls['Item model number'] and fls2['Model Name']:
            ls.append("Modal Name"+ "          :     " + fls['Item model number'])
            ls2.append("Modal Name"+ "          :     " + fls2["Model Name"])
    except:
        pass
    try:
        if fls['Wireless communication technologies'] and (fls2['Wi-Fi'] and fls2['Bluetooth Support']):
            ls.append("Wireless communication technologies"+ "          :     " + fls['Wireless communication technologies'] )
            ls2.append("Wireless communication technologies"+ "          :     " + fls['Wireless communication technologies'] )
    except:
        pass
    try:
        if fls['Connectivity technologies'] and (fls2['Bluetooth Version'] and fls2['Wi-Fi Version'] and fls2['GPS Support'] and fls2['Micro USB Port']):
            print('in')
            ls.append("Connectivity technologies"+ "          :     " + fls['Connectivity technologies'])
            ls2.append("Connectivity technologies"+ "          :     " + "wifi:"+fls2['Wi-Fi Version'] +"; Bluetooth"+fls2['Bluetooth Version']+"; GPS:"+ fls2['GPS Support']+'; USB: '+fls2['Micro USB Port'])
    except:
        pass
    try:
        if fls['Audio Jack'] and fls2['Audio Jack']:
            ls.append("Audio Jack(mm)" + "          :     " + fls['Audio Jack'])
            ls2.append("Audio Jack(mm)" + "          :     " + fls2["Audio Jack"])
    except:
        pass


    data = {
        'name': name,
        'price': price,
        'url': url,
        'ls': ls,
        'name2': name2,
        'price2': price2,
        'ls2': ls2,
        'url2': url2,
    }
    return render(request, 'compare.html', data)
