from django.contrib import admin
from .models import Message

# Register your models here.

class MessageAdmin(admin.ModelAdmin):
    list_display=('name','email','message','active','posted_time')
    list_editable=('email','active')
    list_filter=('active','posted_time')
    search_fields=('name','message')

    ordering=('-posted_time',)

admin.site.register(Message,MessageAdmin)