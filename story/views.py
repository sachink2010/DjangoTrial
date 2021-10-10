
from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib import messages
from .forms import StoryForm
#from .models import Product

# Create your views here.
#https://www.youtube.com/watch?v=eLT2W7nnE28

def say_hello(request):
    #x=1
    #y=2
    #products=Product.objects.all()
    #return render(request,'hello.html',{'name':'Sachin','products':products})
    return render(request,'hello.html',{'name':'Sachin'})

def story(request):
    form=StoryForm(request.POST or None)
    if form.is_valid():
            form.save()
            messages.success(request,'form has been saved successfully')
            return redirect ('/story/story',messages)
    return render(request,'story.html',{'form':form})

