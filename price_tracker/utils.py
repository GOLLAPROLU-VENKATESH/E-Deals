import bs4
import requests
import lxml


def get_link_data(url):
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.141 Safari/537.36",
        "Accept-Language": "en"
    }
    try:
        r = requests.get(url, headers=headers)
        soup = bs4.BeautifulSoup(r.text, "lxml")
        error=0
    except:
        error = 1
        name=" "
        newprice=0

    if error!=1:
        try:
            name = soup.select_one(selector="#productTitle").getText()
            name = name.strip()

            price = soup.select_one(selector="#priceblock_ourprice").getText()
            price = price[2:]
            newprice = ''
            for i in range(len(price)):
                if price[i] == ",":
                    continue
                else:
                    newprice = newprice + price[i]
            newprice = float(newprice)
            error = 0
        except:
            try:
                price = soup.find(class_='_30jeq3 _16Jk6d').getText()
                name = soup.select_one('.yhB1nd').getText()
                price = price[1:]
                newprice = ''
                for i in range(len(price)):
                    if price[i] == ",":
                        continue
                    else:
                        newprice = newprice + price[i]
                newprice = float(newprice)
                error = 0
            except AttributeError:
                try:
                    name = soup.find(class_='pdp-e-i-head').getText()
                    name = name.strip()
                    price = soup.find(class_='payBlkBig').getText()
                    newprice = float(price)
                    error=0
                except:
                    error=1
                    name=" "
                    newprice=0
                    pass
    return name,newprice,error
