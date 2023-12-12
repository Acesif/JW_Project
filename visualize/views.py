from django.shortcuts import render,redirect
from .models import stockModel
import plotly.express as px
import plotly.graph_objects as go
from plotly.subplots import make_subplots

def home(request):
    items = stockModel.objects.all()
    fig = make_subplots(specs=[[{"secondary_y": True}]])

    fig.add_trace(
            go.Scatter(x=[i.date for i in items[:100]], y=[i.close for i in items[:100]], name="close"),
        secondary_y=True,
    )

    fig.add_trace(
            go.Bar(x=[i.date for i in items[:100]], y=[i.volume for i in items[:100]], name="volume"),
        secondary_y=False,
    )

    fig.update_layout(
        title_text="Close/Volume vs Date Graph"
    )

    chart = fig.to_html()
    latest = items[::-1]
    return render(request, 'base.html', {"items": latest[:20], "chart": chart})

def add(request):
    return render(request,'add.html')

def addreq(request):
    date=request.POST['date']
    trade_code=request.POST['trade_code']
    high=request.POST['high']
    low=request.POST['low']
    open=request.POST['open']
    close=request.POST['close']
    volume=request.POST['volume']
    entry=stockModel(date=date,trade_code=trade_code,high=high,low=low,open=open,close=close,volume=volume)
    entry.save()
    return redirect("/")

def update(request,id):
    entry=stockModel.objects.get(id=id)
    return render(request,'update.html',{'entry': entry})

def upreq(request,id):
    date=request.POST['date']
    trade_code=request.POST['trade_code']
    high=request.POST['high']
    low=request.POST['low']
    open=request.POST['open']
    close=request.POST['close']
    volume=request.POST['volume']
    entry=stockModel.objects.get(id=id)
    entry.date=date
    entry.trade_code=trade_code
    entry.high=high
    entry.low=low
    entry.open=open
    entry.volume=volume
    entry.save()
    return redirect("/")


def delete(request,id):
    item=stockModel.objects.get(id=id)
    item.delete()
    return redirect("/")
