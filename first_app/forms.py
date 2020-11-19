from django import forms

from first_app.models import userinfo

from django.contrib.auth.models import User


class UserInfoForm(forms.ModelForm):
    password=forms.CharField(widget=forms.PasswordInput())
    class Meta:
        model=User
        fields=('username','email','password')


class UserPortfolioForm(forms.ModelForm):
    class Meta:
        model=userinfo
        fields=('user_portfolio','user_photo')
