
from django.urls import path
from AdminDash import views

urlpatterns = [
    path('adminHome/', views.adminHome,name='admin_home'),
    path('adminLoginProcess/', views.adminLoginProcess, name='admin_login_process'),
    path('adminLogoutProcess/', views.adminLogoutProcess, name='admin_logout_process'),
  
]
