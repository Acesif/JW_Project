from django import forms
from .models import stockModel


class TradeCodeForms(forms.Form):
    tc=stockModel.objects.all()
    tc=set([i.trade_code for i in items[:100])

    trade_code=forms.CharField(
        label="Select a trade code",
        widget=forms.Select(
           choices=tc 
        )
    )
