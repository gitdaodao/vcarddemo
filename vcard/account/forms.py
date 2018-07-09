from django import forms
from django.contrib.auth.models import User
from .models import Profile

class LoginForm(forms.Form):
    username=forms.CharField(label='用户名')
    password=forms.CharField(label='密码',widget=forms.PasswordInput)


class UserRegisterForm(forms.ModelForm):

    password=forms.CharField(label='密码',widget=forms.PasswordInput)
    re_password=forms.CharField(label='重复密码',widget=forms.PasswordInput)
    class Meta:
        model=User
        fields=('username','email','first_name')

    def clean_re_pwd(self):
        cd=self.creaned_data
        if cd['password'] !=cd['re_password']:
            raise forms.ValidationError('两次密码输入不一致~')
        return cd['re_password']


class UserEditForm(forms.ModelForm):
    class Meta:
        model=User
        fields=('first_name','last_name','email')


class ProfileEditForm(forms.ModelForm):
    class Meta:
        model=Profile
        fields=('Mobile','photo')
        