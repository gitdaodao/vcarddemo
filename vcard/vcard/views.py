from django.shortcuts import render,redirect,reverse
from guestbook.models import Message
from django.http import HttpResponse

def home(request):
    return render(request,'index.html')


