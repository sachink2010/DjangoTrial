from django.contrib import admin

# Register your models here.
# Register your models here.
from .models import Story

class StoryFormAdmin(admin.ModelAdmin):
    readonly_fields = ('created_at',)
    list_display=('user_input','api_response','created_at','username')
    

admin.site.register(Story,StoryFormAdmin)
