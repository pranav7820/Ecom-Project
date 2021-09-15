from django.shortcuts import render
from django.http import HttpResponse
from . models import Product
from math import ceil

def index(request):
    products= Product.objects.all()
    n= len(products)
    nSlides= n//4 + ceil((n/4) + (n//4))
    params={'no_of_slides':nSlides, 'range':range(1,nSlides), 'product': products}
    return render(request,"shop/index.html", params)
def about(request):
    return render(request, 'shop/about.html')
def contact(request):
    return render(request, 'shop/contact.html')
def tracker(request):
    return HttpResponse("we are at tracker")
def search(request):
    return HttpResponse("we are at search")
def productView(request):
    return HttpResponse("we are at aboprdVut")
def checkout(request):
    return HttpResponse("we are at chk")
