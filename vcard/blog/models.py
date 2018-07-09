from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from django.shortcuts import reverse
# from tinymce.models import HTMLField
from taggit.managers import TaggableManager

# Create your models here.

class Category(models.Model):
    name=models.CharField('分类名',max_length=50)
    slug=models.SlugField('url缩写',max_length=100)
    description=models.TextField('备注说明',max_length=300,null=True)

    def __str__(self):
        return self.name


class Post(models.Model):
    STATUS_CHOICES=(
        ('draft','草稿'),
        ('published','发布'),
    )
    title=models.CharField('文章标题',max_length=200)
    slug=models.SlugField('url缩写',max_length=100,unique_for_date='publish')

    category=models.ForeignKey(Category,related_name='blog_posts',null=True,on_delete=models.SET_NULL)
    author=models.ForeignKey(User,related_name='blog_posts',null=True,on_delete=models.SET_NULL)

    body=models.TextField('正文')
    # body=HTMLField('正文')
    image=models.ImageField('图片',null=True,blank=True,upload_to='uploads/')

    publish=models.DateTimeField('发布时间',default=timezone.now)
    created=models.DateTimeField('创建时间',auto_now_add=True)
    updated=models.DateTimeField('更新时间',auto_now=True)
    status=models.CharField('文章状态',choices=STATUS_CHOICES,default='draft',max_length=100)

    tags=TaggableManager()


    def __str__(self):
        return self.title


    class Meta:
        ordering=['-publish']

    # def get_absolute_url(self):
    #     return reverse('blog:blog_detail',args=[
    #             self.publish.year,
    #             self.publish.month,
    #             self.publish.day,
    #             self.slug
    #     ])


class Comment(models.Model):
    post=models.ForeignKey(Post,related_name='comments',null=True,on_delete=models.SET_NULL)
    name=models.CharField('姓名',max_length=100)
    email=models.EmailField('邮箱',max_length=100)
    message=models.TextField('消息')
    active=models.BooleanField('是否有效',default=True)
    created=models.DateTimeField('提交时间',auto_now_add=True)

    class Meta:
        ordering=['-created']

    def __str__(self):
        return f'{self.name}对{self.post}有评论' 




