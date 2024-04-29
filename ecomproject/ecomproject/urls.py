from django.conf import settings
from django.conf.urls.static import static

from django.contrib import admin
from django.urls import path

from carrinho.views import menu_carrinho
from core.views import principal, moveis, cadastro, login
from produtos.views import produto

urlpatterns = [
    path('', principal, name='principal'),
    path('cadastro/', cadastro, name='cadastro'),
    path('login/', login, name='login'),
    path('moveis/', moveis, name='moveis'),
    path('produto/<slug:slug>/', produto, name='produto'),
    path('menu_carrinho/<int:produto_id>/', menu_carrinho, name='menu_carrinho'),
    path('admin/', admin.site.urls),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
