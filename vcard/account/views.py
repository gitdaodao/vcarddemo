from django.shortcuts import render,redirect,reverse
from .forms import LoginForm
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
from .forms import *
from django.contrib import messages

# Create your views here. (login_url='account:user_login')
def home(request): 
    return render(request,'account/base.html')

@login_required(login_url='/account/login/')
def user_dashboard(request):
    return render(request,'account/bashboard.html')


def user_login(request):
    if request.method=='POST':
        form=LoginForm(request.POST)
        if form.is_valid():
            data=form.cleaned_data
            username=data['username']
            pwd=data['password']
            # 验证用户信息 如对上说明是可登录用户 
            user=authenticate(username=username,password=pwd)
            if user:
                if user.is_active:
                    # 是激活用户 给会员全站通行权限
                    login(request,user)
                    return redirect(reverse('account:user_dashboard'))
                else:
                    return HttpResponse('用户被锁定~')
            return HttpResponse('用户名或者密码错误')
    form=LoginForm()
    return render(request,'account/login.html',{'form':form})


def user_logout(request):
    logout(request)
    return redirect(reverse('account:user_login'))

def register(request):
    if request.method=='POST':
        user_form=UserRegisterForm(request.POST)
        if user_form.is_valid():
            u=user_form.save(commit=False)
            # 给实列化用户u 进行密码字段哈希u.set_password()
            u.set_password(user_form.cleaned_data['password'])
            u.save()
            return render(request,'account/register_done.html',{'new_user':u})
    user_form=UserRegisterForm()
    return render(request,'account/register.html',{'user_form':user_form})


@login_required
def edit(request):
    if request.method=='POST':
        user_form=UserEditForm(instance=request.user,data=request.POST)
        profile_form=ProfileEditForm(instance=request.user.profile,data=request.POST,files=request.FILES)
        if user_form.is_valid() and profile_form.is_valid():
            user_form.save()
            profile_form.save()
            messages.success(request,'个人资料更新成功')
        else:
            messages.error(request,'个人资料更新失败,请重试~')
    else:
        user_form=UserEditForm(instance=request.user)
        profile_form=ProfileEditForm(instance=request.user.profile)
    return render(request,'account/edit.html',{'user_form':user_form,'profile_form':profile_form})