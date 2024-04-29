from django.urls import path

from .views import *

urlpatterns = [
    path('produto/<slug:slug>/', produto, name='produto'),
]