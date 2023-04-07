from django.shortcuts import render
from .models import New


# Create your views here.
def index(request):
    news = New.objects.order_by('-data_pub')  # от более свежей к самой старой
    return render(request, 'default.html', {'news': news})


def detail(reguest, slug):
    new = New.objects.get(slug__iexact=slug)  # ищем точное совпадение slug
    return render(reguest, 'detail.html', context={'new': new})
