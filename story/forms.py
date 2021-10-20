from django import forms
#from django.forms import ModelForm
#from django,forms import forms
from django.forms.widgets import Widget
from .models import Story
#from django.forms import Form


# Create the form class.
class StoryForm(forms.ModelForm):
    class Meta:
        model = Story
        fields=['user_input','username']

        widgets={
            'user_input':forms.Textarea(attrs={'class':'form-control','help_text':'Please fill up 1-2 lines'}),
            'username':forms.TextInput(attrs={'class':'form-control'}),
            #'api_response':forms.Textarea(attrs={'class':'form-control', 'disabled':'True'})
        }
    
    
