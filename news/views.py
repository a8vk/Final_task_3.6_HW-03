from django.shortcuts import render
from .models import New


# Create your views here.
def index(request):
    news = New.objects.order_by('-data_pub')  # от более свежей к самой старой
    return render(request, 'default.html', {'news': news})


def detail(request, pk):
    new = New.objects.get(pk=pk)
    return render(request, 'detail.html', context={'new': new})
