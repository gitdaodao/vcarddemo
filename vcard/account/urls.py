from django.urls import path
from .views import *

app_name='account'

urlpatterns=[
    path('',home,name='home'),
    path('dashboard/',user_dashboard,name='user_dashboard'),
    path('login/',user_login,name='user_login'),
    path('logout/',user_logout,name='user_logout'),
    path('register/',register,name='register'),
    path('edit/',edit,name='edit'),
]