from django.urls import path

from django.contrib.auth import views #login

from .views import *

urlpatterns = [
    path('', principal, name='principal'),
    path('cadastro/', cadastro, name='cadastro'),
    path('logout/', custom_logout, name='logout'),
    path('login/', views.LoginView.as_view(template_name='core/login.html'), name='login'),
    path('moveis/', moveis, name='moveis'),
]