from django.shortcuts import render,get_object_or_404
from .models import Category,Post,Comment
from django.db.models import Count
from django.core.paginator import Paginator,EmptyPage,PageNotAnInteger
from taggit.models import Tag


# Create your views here.

def blog_list(request,cslug=None):
    """博客列表页"""
    object_list=Post.objects.filter(status='published')
    if cslug:
        category=get_object_or_404(Category,slug=cslug)
        object_list=object_list.filter(category=category)
    paginator=Paginator(object_list,5)
    page=request.GET.get('page')
    try:    
        posts=paginator.page(page)
    except PageNotAnInteger:
        posts=paginator.page(1)
    except EmptyPage:
        posts=paginator.page(paginator.num_pages)
    return render(request,'blog/blog-list.html',{'page':page,'posts':posts,'paginator':paginator})


def blog_list_by_tag(request,ytag=None):
    object_list=Post.objects.filter(status='published')
    if ytag:
        tag=get_object_or_404(Tag,tag=ytag)
        object_list=object_list.filter(tags=tag)
    paginator=Paginator(object_list,5)
    page=request.GET.get('page')
    try:    
        posts=paginator.page(page)
    except PageNotAnInteger:
        posts=paginator.page(1)
    except EmptyPage:
        posts=paginator.page(paginator.num_pages)
    return render(request,'blog/blog-list.html',{'page':page,'posts':posts,'paginator':paginator})


def blog_detail(request,slug):
    post=get_object_or_404(Post,slug=slug)
    """相关日志"""
    post_tags_ids = post.tags.values_list('id',flat=True)
    similar_posts = Post.objects.filter(tags__in= post_tags_ids).exclude(id = post.id)
    similar_posts = similar_posts.annotate(same_tags = Count('tags')).order_by('-same_tags','-publish')[:4]
    return render(request,'blog/blog-detail.html',{'post':post,'similar_posts':similar_posts})