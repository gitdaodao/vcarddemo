from django.urls import path
from .views import *

app_name ='blog'

urlpatterns=[
    path('',blog_list,name='blog_list'),
    path('<slug:cslug>/',blog_list,name='blog_list_by_cslug'),
    path('',blog_list_by_tag,name='blog_list_by_tag'),
    path('detail/<slug:slug>/',blog_detail,name='blog_detail'),
]