
from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib import messages
from .forms import StoryForm, CodeForm
import requests
import openai
import os
#from rest_framework.views import APIView




#from .models import Product

# Create your views here.
#https://www.youtube.com/watch?v=eLT2W7nnE28
#https://www.youtube.com/watch?v=iySjsCPgTPg

def intro(request):
    return render(request,'intro.html',{'name':'Sachin'})

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
            jurassic_key="Bearer eNZ1QKmraxGN9f41ESRL6MZ9zLxzCOwE"

            #print(jurassic_key)
            
            response=requests.post(
                "https://api.ai21.com/studio/v1/j1-jumbo/complete",
                headers={"Authorization": jurassic_key},
                json={
                    "prompt": user_input, 
                    "numResults": 1, 
                    "maxTokens": 50, 
                    "topKReturn": 0,
                    "temperature": 0.7,
                    #"stopSequences": ["\n"],
                    }
                )
            data = response.json()
            #print(data)
            tokens = [t['generatedToken']['token'] for t in data['completions'][0]['data']['tokens']]
            #print(tokens)
            #print("****************")
            #print("".join(tokens).replace("▁"," ").replace("<|newline|>", "\n"))
            response_text="".join(tokens).replace("▁"," ").replace("<|newline|>", "\n")
            #print("****************")

            #print(response_text)
            postform.api_response=response_text
            #form.cleaned_data['api_response']=response_text
            #print(form.api_response)
            #print(response_text)
            postform.save()
            response_text=response_text
            #form.cleaned_data['user_input']=response_text
            #form.save
            messages.success(request,'form has been saved successfully')
           
            #print('form is',form['user_input'])
            #return redirect('/story/story', {'form':form})
            return render(request,'story.html', {'response_text':response_text, 'form':form})

    return render(request,'story.html',{'form':form})

def code(request):
    form=CodeForm(request.POST or None)
    dict=(request.POST).dict()

    print(dict)
    print(type(dict))
    #print(dict['username'])
    if form.is_valid():
            
            postform=form.save(commit=False)
            username=dict['username']
            user_input=dict['user_input']
            print(f'username is,', {username})

           
            openai.api_key = os.environ['OPENAI_KEY']


            response = openai.Completion.create(
                engine="davinci-codex",
                prompt=user_input,
                temperature=0,
                max_tokens=200,
                top_p=1.0,
                frequency_penalty=0.0,
                presence_penalty=0.0,
                stop=["\"\"\""]
                )
           
            data = response.choices[0].text
            print(data)
            response_text=data
            print("****************")

            print(response_text)
            postform.api_response=response_text
            #form.cleaned_data['api_response']=response_text
            #print(form.api_response)
            #print(response_text)
            postform.save()
            response_text=response_text
            #form.cleaned_data['user_input']=response_text
            #form.save
            messages.success(request,'form has been saved successfully')
           
            #print('form is',form['user_input'])
            #return redirect('/story/story', {'form':form})
            return render(request,'code.html', {'response_text':response_text, 'form':form})

    return render(request,'code.html',{'form':form})

