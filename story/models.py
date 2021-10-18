from django.db import models

# Create your models here.
class Story(models.Model):
    user_input = models.CharField(max_length=200)
    api_response = models.CharField(max_length=2000, null=True, blank=True)
    #timestamp=models.DateTimeField
    created_at = models.DateTimeField(auto_now_add=True)
    username = models.CharField(max_length=200)
