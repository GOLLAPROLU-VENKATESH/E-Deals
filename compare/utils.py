import bs4
import requests
import lxml


# url='https://www.flipkart.com/technoview-full-hd-1080p-webcam-pc-laptop-desktop-usb-microphone-video-conferencing-calls-compatible-skype-facetime-hangouts-plug-play/p/itm257f6cd2a2772?pid=ACCFUTQCEAXRPFPE&lid=LSTACCFUTQCEAXRPFPE5OQDPI&marketplace=FLIPKART&store=6bo%2Fai3%2Fr3e&srno=b_1_1&otracker=hp_omu_Best%2Bof%2BElectronics_3_12.dealCard.OMU_J7IYP0MVPUYF_8&otracker1=hp_omu_WHITELISTED_neon%2Fmerchandising_Best%2Bof%2BElectronics_NA_dealCard_cc_3_NA_view-all_8&fm=neon%2Fmerchandising&iid=en_eM8EobvhEDut1JBhEhH7xWuWnKNEWMCWgSu9mQ3dPShYAZLmsEDOqVRlv7MtTGTrafmoNXcVHq%2FM8kmM5TBQ2A%3D%3D&ppt=hp&ppn=homepage&ssid=9op7zvup4w0000001621345343918'

def get_link_data(url):
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.141 Safari/537.36",
        "Accept-Language": "en"
    }
    r = requests.get(url, headers=headers)
    soup = bs4.BeautifulSoup(r.text, "lxml")
    try:
        name = soup.select_one(selector="#productTitle").getText()
        name = name.strip()
        try:
            price = soup.select_one(selector="#priceblock_ourprice").getText()
            price = price[2:]
            newprice = ''
            for i in range(len(price)):
                if price[i] == ",":
                    continue
                else:
                    newprice = newprice + price[i]
            newprice = float(newprice)
        except:
            price = soup.select_one(selector="#priceblock_dealprice").getText()
            price = price[2:]
            newprice = ''
            for i in range(len(price)):
                if price[i] == ",":
                    continue
                else:
                    newprice = newprice + price[i]
            newprice = float(newprice)
        th = soup.find_all(class_="a-color-secondary a-size-base prodDetSectionEntry")
        ls=[]
        for m in th:
            n=m.getText()
            n=n.strip()
            if n=='ASIN':
                break
            else:
                 b=m.getText()
                 b=b.strip()
                 ls.append(b)
        ls2=[]
        td = soup.find_all(class_="a-size-base prodDetAttrValue")
        count = 0
        for f in td:
            if count is len(ls):
                break
            else:
                c = f.getText()
                c = c.strip()
                ls2.append(c)
                count=count+1
        fls = {}
        for a in range(len(ls)):
            fls[ls[a]] = ls2[a]
    except:
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
        th = soup.find_all(class_="_1hKmbr col col-3-12")
        td = soup.find_all(class_="_21lJbe")
        fls=[]
        fls = {}
        for a in range(len(td)):
            fls[th[a].getText()] = td[a].getText()
    return name,newprice,fls