from django.db import models

# Create your models here.
class Story(models.Model):
    request = models.CharField(max_length=200)
    response = models.CharField(max_length=2000)
    #timestamp=models.DateTimeField
    created_at = models.DateTimeField(auto_now_add=True)
    username = models.CharField(max_length=200)
