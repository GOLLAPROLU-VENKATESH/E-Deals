from django.shortcuts import render
from .models import Techblog


# Create your views here.
def tblog(request):
    blog=Techblog.get_all_techblog()
    data = {}
    data['blog'] = blog
    return render(request,'techblog.html',data)

def vblog(request):
    postData = request.POST
    bid= postData.get('bid')
    data = {}
    blog=Techblog.get_blog_by_id(bid)
    data['vblog'] = blog
    return render(request,'blog.html',data)