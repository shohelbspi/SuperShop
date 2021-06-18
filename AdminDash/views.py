from django.http.response import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from django.contrib.auth import authenticate,login, logout
from django.contrib import messages
from django.urls import reverse
from django.contrib.auth.decorators import login_required

# Create your views here.

def adminLogin(request):
    return render(request,'backend/Admin/login.html')

@login_required(login_url='/admin')
def adminHome(request):
    return render(request,'backend/Admin/home.html')

def adminLoginProcess(request):
    username = request.POST.get('username')
    password = request.POST.get('password')

    user = authenticate(username=username, password=password)

    if user is not None:
        login(request, user=user)
        return HttpResponseRedirect(reverse('admin_home'))
        
    else:
        messages.error(request, 'Error in Login ! Invalid Login Details')
        return HttpResponseRedirect(reverse('admin_login'))


def adminLogoutProcess(request):

    logout(request)
    messages.success(request,'SuccessFully Logout !')
    return HttpResponseRedirect(reverse('admin_login'))