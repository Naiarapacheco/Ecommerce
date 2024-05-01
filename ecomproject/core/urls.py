from django.urls import path

from django.contrib.auth import views #login

from .views import *
from produtos.views import produto 

urlpatterns = [
    path('', principal, name='principal'),
    path('cadastro/', cadastro, name='cadastro'),
    path('logout/', custom_logout, name='logout'),
    path('login/', views.LoginView.as_view(template_name='core/login.html'), name='login'),
    path('minhaconta/', minhaconta, name="minhaconta"),
    path('editar_minhaconta/', editar_minhaconta, name="editar_minhaconta"),
    path('moveis/', moveis, name='moveis'),
    path('produto/<slug:slug>/', produto, name='produto'),
]