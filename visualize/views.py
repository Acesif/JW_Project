from django.shortcuts import render
import json
import os
from django.conf import settings

file_path = os.path.join(settings.BASE_DIR, 'visualize/stock_market_data.json')

def home(request):
    with open(file_path) as f:
        json_data = json.load(f)

    return render(request, 'base.html', {'json_data': json_data})

