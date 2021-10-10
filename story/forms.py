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
        fields=['request','username']

        widgets={
            'request':forms.Textarea(attrs={'class':'form-control'}),
            'username':forms.TextInput(attrs={'class':'form-control'})
        }
    
    
