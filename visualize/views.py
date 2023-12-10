from django.shortcuts import render
from .models import stockModel

def home(request):
    items = stockModel.objects.all()
    return render(request, 'base.html', {"items": items})

