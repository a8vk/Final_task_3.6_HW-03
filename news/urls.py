from django.urls import path
from .views import index, detail

urlpatterns = [
    path('', index, name='default'),
    path('<int:pk>', detail, name='detail'),
]
