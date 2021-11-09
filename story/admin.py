from django.contrib import admin

# Register your models here.
# Register your models here.
from .models import Story, Code

class StoryFormAdmin(admin.ModelAdmin):
    readonly_fields = ('created_at',)
    list_display=('user_input','api_response','created_at','username')
    

admin.site.register(Story,StoryFormAdmin)

class CodeFormAdmin(admin.ModelAdmin):
    readonly_fields = ('created_at',)
    list_display=('user_input','api_response','created_at','username')
    

admin.site.register(Code,CodeFormAdmin)