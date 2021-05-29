import base64
from django.shortcuts import render, redirect
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sb
from io import BytesIO
from store.models.category import Category
from store.models.estore import Estore


def graphs(request):
    es = pd.DataFrame(Estore.objects.all().values())
    ca = pd.DataFrame(Category.objects.all().values())
    plt.switch_backend('AGG')
    fig = plt.figure(figsize=(12, 5))
    font1 = {'family': 'serif', 'color': 'blue', 'size': 20}
    font2 = {'family': 'serif', 'color': 'darkred', 'size': 15}
    title = 'Estore Stats'
    plt.title(title,fontdict=font1)
    if request.GET.get('esl'):
        plt.plot(es['name'], es['count'],marker='*')
        plt.xlabel("Estores",fontdict=font2)
        plt.ylabel("No views",fontdict=font2)
        buffer = BytesIO()
        plt.savefig(buffer, format='png')
        buffer.seek(0)
        image_png = buffer.getvalue()
        graph = base64.b64encode(image_png)
        graph = graph.decode('utf-8')
        buffer.close()
    elif request.GET.get('ess'):
        plt.scatter(es['name'], es['count'])
        plt.xlabel("Estores",fontdict=font2)
        plt.ylabel("No views",fontdict=font2)
        buffer = BytesIO()
        plt.savefig(buffer, format='png')
        buffer.seek(0)
        image_png = buffer.getvalue()
        graph = base64.b64encode(image_png)
        graph = graph.decode('utf-8')
        buffer.close()
    elif request.GET.get('esp'):
        plt.pie(es['count'],labels=es['name'])
        buffer = BytesIO()
        plt.savefig(buffer, format='png')
        buffer.seek(0)
        image_png = buffer.getvalue()
        graph = base64.b64encode(image_png)
        graph = graph.decode('utf-8')
        buffer.close()
    else:
        plt.bar(es['name'], es['count'])
        plt.xlabel("Estores",fontdict=font2)
        plt.ylabel("No views",fontdict=font2)
        buffer = BytesIO()
        plt.savefig(buffer, format='png')
        buffer.seek(0)
        image_png = buffer.getvalue()
        graph = base64.b64encode(image_png)
        graph = graph.decode('utf-8')
        buffer.close()
    if request.GET.get('cal'):
        fig = plt.figure(figsize=(13, 5))
        plt.plot(ca['name'], ca['count'],marker='*')
        plt.xlabel("Category",fontdict=font2)
        plt.ylabel("No views",fontdict=font2)
        title = 'Category Stats'
        plt.title(title, fontdict=font1)
        buffe = BytesIO()
        plt.savefig(buffe, format='png')
        buffe.seek(0)
        image_pn = buffe.getvalue()
        graph2 = base64.b64encode(image_pn)
        graph2 = graph2.decode('utf-8')
        buffe.close()
    elif request.GET.get('cas'):
        fig = plt.figure(figsize=(13, 5))
        plt.scatter(ca['name'], ca['count'])
        plt.xlabel("Category",fontdict=font2)
        plt.ylabel("No views",fontdict=font2)
        title = 'Category Stats'
        plt.title(title, fontdict=font1)
        buffe = BytesIO()
        plt.savefig(buffe, format='png')
        buffe.seek(0)
        image_pn = buffe.getvalue()
        graph2 = base64.b64encode(image_pn)
        graph2 = graph2.decode('utf-8')
        buffe.close()
    elif request.GET.get('cap'):
        plt.figure()
        plt.xlabel(" ", fontdict=font2)
        plt.ylabel(" ", fontdict=font2)
        title = ''
        plt.title(title, fontdict=font1)
        plt.pie(ca['count'], labels=ca['name'])
        buffe = BytesIO()
        plt.savefig(buffe, format='png')
        buffe.seek(0)
        image_pn = buffe.getvalue()
        graph2 = base64.b64encode(image_pn)
        graph2 = graph2.decode('utf-8')
        buffe.close()
    else:
        fig = plt.figure(figsize=(13, 5))
        plt.bar(ca['name'], ca['count'],align='center',width=0.8)
        title = 'Category Stats'
        plt.title(title, fontdict=font1)
        plt.xlabel("Category",fontdict=font2)
        plt.ylabel("No views",fontdict=font2)
        buffe = BytesIO()
        plt.savefig(buffe, format='png')
        buffe.seek(0)
        image_pn = buffe.getvalue()
        graph2 = base64.b64encode(image_pn)
        graph2 = graph2.decode('utf-8')
        buffe.close()
    contex = {
        'es': es,
        'ca': ca,
        'graph': graph,
        'graph2':graph2,
    }
    return render(request, 'stats.html', contex)
