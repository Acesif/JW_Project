from django.shortcuts import render
from .models import stockModel
import plotly.express as px
import plotly.graph_objects as go
from plotly.subplots import make_subplots

def home(request):
    items = stockModel.objects.all()
    return render(request, 'base.html', {"items": items[:20]})

def chart(request):
    items = stockModel.objects.all() 
    trade_code = set([i.trade_code for i in items[:100]])
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

    fig.update_xaxes(title_text="Date")

    chart = fig.to_html()
    return render(request, 'chart.html', {'chart': chart, 'tc': trade_code})

