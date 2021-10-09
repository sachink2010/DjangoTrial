from django.forms import ModelForm
from .models import Story


# Create the form class.
class StoryForm(ModelForm):
    class Meta:
        model = Story
        fields=['request','username']
    
