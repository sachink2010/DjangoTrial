
from django.shortcuts import render
from django.http import HttpResponse
#from .models import Product

# Create your views here.

def say_hello(request):
    #x=1
    #y=2
    #products=Product.objects.all()
    #return render(request,'hello.html',{'name':'Sachin','products':products})
    return render(request,'hello.html',{'name':'Sachin'})

    #return HttpResponse('Hello World')

