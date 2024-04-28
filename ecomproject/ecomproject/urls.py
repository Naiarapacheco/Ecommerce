from django.contrib import admin
from django.urls import path, include


from core.views import principal

urlpatterns = [
    path('', principal, name='principal'),
    path('admin/', admin.site.urls),
]
