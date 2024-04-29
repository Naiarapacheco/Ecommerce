from django.conf import settings
from django.conf.urls.static import static

from django.contrib import admin
from django.contrib.auth import views #logoutview
from django.urls import path

from carrinho.views import add_carrinho, carrinho, checkout
from core.views import principal, moveis, cadastro, custom_logout
from produtos.views import produto

urlpatterns = [
    path('', principal, name='principal'),
    path('cadastro/', cadastro, name='cadastro'),
    path('logout/', custom_logout, name='logout'),
    path('login/', views.LoginView.as_view(template_name='core/login.html'), name='login'),
    path('moveis/', moveis, name='moveis'),
    path('produto/<slug:slug>/', produto, name='produto'),
    path('carrinho-compras/', carrinho, name='carrinho'),
    path('checkout/', checkout, name='checkout'),
    path('menu_carrinho/<int:produto_id>/', add_carrinho, name='add_carrinho'),
    path('admin/', admin.site.urls),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
