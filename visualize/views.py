from django.shortcuts import render
from .models import stockModel
import plotly.express as px

def home(request):
    items = stockModel.objects.all()
    return render(request, 'base.html', {"items": items})

def chart(request):
    items = stockModel.objects.all() 
    fig = px.line(
        x=[i.date for i in items],
        y=[i.close for i in items],
    )
    chart = fig.to_html()
    return render(request, 'chart.html', {'chart': chart})

