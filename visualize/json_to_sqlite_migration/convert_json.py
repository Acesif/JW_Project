import json
import copy
with open('stock_market_data.json') as dataf, open('output.json', 'w') as out:
    data = json.load(dataf)
    newdata = []
    for i, block in enumerate(data):
        new = dict(model="visualize.stockModel", pk=i+1)
        new['fields'] = dict(
            date=block['date'],
            trade_code=block['trade_code'],
            high=block['high'],
            low=block['low'],
            open=block['open'],
            close=block['close'],
            volume=block['volume']
        )
        newdata.append(copy.deepcopy(new))
    json.dump(newdata, out, indent=2)
