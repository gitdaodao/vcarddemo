from django import template
from blog.models import Post,Category
from taggit.models import Tag

register=template.Library()


@register.simple_tag
def total_posts():
    return Post.objects.filter(status='published').count()


@register.inclusion_tag('blog/latest_posts.html')
def show_latest_posts(count=5):
    """包含标签"""
    latest_posts=Post.objects.filter(status='published').order_by('-publish')[:count]
    return {'latest_posts':latest_posts}


@register.simple_tag
def get_all_categories(): 
    """赋值标签"""
    return Category.objects.all()

@register.simple_tag
def get_all_tags():
    return Tag.objects.all()

