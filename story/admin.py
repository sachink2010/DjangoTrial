from django.contrib import admin

# Register your models here.
# Register your models here.
from .models import Story

class StoryAdmin(admin.ModelAdmin):
    readonly_fields = ('created_at',)
    list_display=('request','response','created_at','username')
    

admin.site.register(Story,StoryAdmin)
