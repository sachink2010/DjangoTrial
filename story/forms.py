from django import forms
#from django.forms import ModelForm
#from django,forms import forms
from django.forms.widgets import Widget
from .models import Story, Code
#from django.forms import Form


# Create the form class.
class StoryForm(forms.ModelForm):
    class Meta:
        model = Story
        fields=['user_input','username']

        widgets={
            'user_input':forms.Textarea(attrs={'class':'form-control','rows':5,'id_for_label':"up to 600 chars",'placeholder':'Please add 1-2 lines of your idea/story, your name and submit'}),
            'username':forms.TextInput(attrs={'class':'form-control','placeholder':'Your name'}),
            #'api_response':forms.Textarea(attrs={'class':'form-control', 'disabled':'True'})
        }
    
class CodeForm(forms.ModelForm):
    class Meta:
        model = Code
        fields=['user_input','username']

        widgets={
            'user_input':forms.Textarea(attrs={'class':'form-control','rows':5,'id_for_label':"up to 600 chars",'placeholder':'Please add 1-2 lines of what you want to code, your name and submit'}),
            'username':forms.TextInput(attrs={'class':'form-control','placeholder':'Your name'}),
            #'api_response':forms.Textarea(attrs={'class':'form-control', 'disabled':'True'})
        }
  