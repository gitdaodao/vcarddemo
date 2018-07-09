from django.shortcuts import render,redirect,reverse
from guestbook.models import Message
from django.http import HttpResponse

# Create your views here.

def post_message(request):
    if request.method=='POST':
        # '' 空字符默认是False
        name=request.POST.get('name','')
        email=request.POST.get('email','')
        message=request.POST.get('message','')
        if name and message:
            msg=Message(name=name,email=email,message=message)
            msg.save()
            return redirect(reverse('home'))
        return HttpResponse('用户名和信息必须填写~')
    return redirect(reverse('home'))
