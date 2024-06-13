from django.shortcuts import render
from django.http import  HttpResponse
# Create your views here.
#from .models import Product
def product(request):
    return HttpResponse("<h1 style='colour:purple'>Using shortcuts. My first webpage with python Django</></>")

def product_list(request):
    
    products= Product.objects.all()
    context = {
        'products':products,
    }
    return render(request,'htmlfile',context)
def product_details(request):
    pass