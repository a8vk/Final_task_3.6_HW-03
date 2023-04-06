from django.urls import path
from .views import index, detail

urlpatterns = [
    path('', index, name='default'),
    path('<str:slug>', detail, name='detail'),
]
