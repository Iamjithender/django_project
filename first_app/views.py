from django.shortcuts import render
from first_app.models import userinfo
from first_app.forms import UserInfoForm,UserPortfolioForm


# from django.contrib.auth.models import User
from django.http import HttpResponse,HttpResponseRedirect
from django.contrib.auth import authenticate,login,logout
from django.urls import reverse
from django.contrib.auth.decorators import login_required
# from django import httpresponse

@login_required
def user_logout(request):
    logout(request)
    return HttpResponseRedirect(reverse('index'))#request,'first_app/index.html',context={})

@login_required
def specialpage(request):
    return HttpResponse("thanks for visiting to special page")



def index(request):
    return render(request,'first_app/index.html',context={})

def registration(request):

    registered=False
    if request.method =='POST':
        infoform=UserInfoForm(data=request.POST)
        portfolioform=UserPortfolioForm(data=request.POST)
        if infoform.is_valid() and portfolioform.is_valid():
            user=infoform.save()
            user.set_password(user.password)
            user.save()
            profile=portfolioform.save(commit=False)
            profile.user=user
            if 'user_photo' in request.FILES:
                profile.user_photo=request.FILES['user_photo']
            profile.save()
            registered=True
        else:
            print("entered details are incorrect once check and execute")
    else:
        infoform=UserInfoForm()
        portfolioform=UserPortfolioForm()
    return render(request,'first_app/registration.html',context={'user':infoform,
                                                            'portfolio':portfolioform,
                                                            'registered':registered})

def user_login(request):

    if request.method == 'POST':
        username=request.POST.get('username')
        password=request.POST.get('password')

        user=authenticate(username=username,password=password)

        if user:
            if user.is_active:
                login(request,user)
                return HttpResponseRedirect(reverse('index'))
            else:
                return HttpReponse("account not active")
        else:
            print("someone tried to login with incorrect details")
            return HttpReponse("invalid login details provided!")
    else:
        return render(request,'first_app/login.html',context={})



# def user_login(request):
#     return render(request,'first_app/index.html',context={})
