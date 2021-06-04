from django.shortcuts import render

# Create your views here.

def adminLogin(request):
    return render(request,'backend/Admin/login.html')

def adminHome(request):
    return render(request,'backend/Admin/home.html')