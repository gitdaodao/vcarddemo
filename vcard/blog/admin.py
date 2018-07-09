from django.contrib import admin
from .models import Category,Post,Comment

# Register your models here.

class CategoryAdmin(admin.ModelAdmin):
    list_display=('name','slug','description')


class PostAdmin(admin.ModelAdmin):
    list_display=('title','slug','author','status','created')
    list_editable=('status',)
    search_fields=('title','body')
    list_filter=('category','status','created')
    list_per_page=10
    # 日期 时间后台管理 友好提示
    date_hierarchy='publish'

    class Media:
        js = (
            'https://cloud.tinymce.com/stable/tinymce.min.js',
            '/static/js/tinymce/custom.js',
        )

    

class CommentAdmin(admin.ModelAdmin):
    list_display=('post','name','name','email','active','created')
    list_per_page=20

admin.site.register(Comment,CommentAdmin)
admin.site.register(Post,PostAdmin)
admin.site.register(Category,CategoryAdmin)
