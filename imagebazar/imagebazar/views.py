
from django.http import HttpResponse
from django.shortcuts import render
from myapp.models import *


def about(request):
    name='arpit'
    city='shahajahanpur'
    adrs='xyz'
    data={ 'name':name,
           'city':city,
           'adrs':adrs
    }
    return render(request,"about.html",data)

def home(request):
    cats=Category.objects.all()
    images = Images.objects.all()
    data = {'images': images, 'cats':cats}
    return render(request, 'home.html',data)

def category(request,cid):
    cats=Category.objects.all()

    category=Category.objects.get(pk=cid)
    print (category)


    images = Images.objects.filter(cat=category)
    data = {'images': images, 'cats':cats}
    return render(request, 'home.html',data)