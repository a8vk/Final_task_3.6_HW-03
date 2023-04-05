from django.shortcuts import render
from .models import New


# Create your views here.
def index(request):
    news = New.objects.all()
    return render(request, 'index.html', context={'news': news})

def detail(reguest, slug):
    new = New.objects.get(slug__iexact=slug)  # ищем точное совпадение slug
    return render(reguest, 'detail.html', context={'new': new})
