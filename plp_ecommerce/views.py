#from django.shortcuts import render
from django.http import  HttpResponse
# Create your views here.
#from .models import Product
def home(request):
    return HttpResponse("<h1>Using shortcuts. My first webpage with python Django</>")

def product_list(request):
    
    products= Product.objects.all()
    context = {
        'products':products,
    }
    return render(request,'plp_ecommerce/product_list.html',context)