from django.shortcuts import render,redirect
from .forms import RegistrationForm
from django.contrib import messages
from django.contrib.auth import login,logout,authenticate
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.views import PasswordChangeView
from django.urls import reverse_lazy


# Create your views here.

def UserRegistration(request):
    # return render(request,'registration.html')
    if request.method =='POST':
        auth = RegistrationForm(request.POST)
        if auth.is_valid():
            auth.save()
            return redirect('homepage')
    else:
        auth= RegistrationForm()
    return render(request,'registration.html',{'form':auth})

def UserLogin(request):
    if request.method=='POST':
        user = request.POST['username']
        password = request.POST['password']
        auth = authenticate(request=request,username=user,password=password)
        if auth is not None:
            form = login(request,auth)
            return redirect('homepage')
        else:
            messages.warning(request,"Password and User name Doesn't exit")
    form = AuthenticationForm()
    return render(request,'login.html',{'form':form})

def UserProfile(request):
    return render(request,'profile.html')

def UserLogout(request):
    logout(request)
    return redirect('homepage')

class ResetYourPassword(PasswordChangeView):
    template_name='resetpassword.html'
    success_url=reverse_lazy('profile')
    

