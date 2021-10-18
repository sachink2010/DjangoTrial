
from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib import messages
from .forms import StoryForm
import requests
import os
#from rest_framework.views import APIView




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
    dict=(request.POST).dict()

    print(dict)
    print(type(dict))
    #print(dict['username'])
    if form.is_valid():
            
            postform=form.save(commit=False)
            username=dict['username']
            user_input=dict['user_input']
            print(f'username is,', {username})
            #jurassic_key=os.environ['JURASSIC_KEY']
            jurassic_key='Bearer eNZ1QKmraxGN9f41ESRL6MZ9zLxzCOwE'
            #print(jurassic_key)
            
            response=requests.post(
                "https://api.ai21.com/studio/v1/j1-jumbo/complete",
                headers={"Authorization": jurassic_key},
                json={
                    "prompt": user_input, 
                    "numResults": 1, 
                    "maxTokens": 50, 
                    "topKReturn": 0,
                    "temperature": 0.7
                    }
                )
            data = response.json()
            tokens = [t['generatedToken']['token'] for t in data['completions'][0]['data']['tokens']]
            response_text="".join(tokens).replace("▁"," ").replace("<|newline|>", "\n")
            postform.api_response=response_text
            #form.cleaned_data['api_response']=response_text
            #print(form.api_response)
            #print(response_text)
            postform.save()
            response_text=user_input+ ''+response_text
            #form.save
            messages.success(request,'form has been saved successfully')
           
            print('form is',form)
            #return redirect('/story/story', {'form':form})
            return render(request,'story.html', {'response_text':response_text, 'form':form})

    return render(request,'story.html',{'form':form})

