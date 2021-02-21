import requests
import pandas
import time 
from datetime import datetime

API_KEY = 'API_KEYOZJ4TPTFAQ3ZIGQ5PBVEDL3DVWRY422Y'
BASE_URL = 'https://api.finage.co.uk/agg/crypto'

symbol = input('Symbol [btcusd, ethusd, ltcusd]: ')
multiply = input('Multiply  [1,2,3,4]: ')
time = input('Time  [minute, hour, day, week, month, quarter, year]: ')
start_date = input('Start date [2020-01-01]: ')
end_date = input('End date [2020-01-07]: ')


API_ENDPOINT = BASE_URL + '/' + symbol + '/' + multiply + '/' + time  + '/' + start_date + '/' + end_date + '?apikey=' + API_KEY

response = requests.get(API_ENDPOINT)


list = []
low = []
high = []


for item in response.json()["results"]:
    element = {
        'open': item['o'],
        'high': item['h'],
        'low': item['l'],
        'close': item['c'],
        'volume': item['v'],
        'date': pandas.to_datetime(item['t'], unit='ms')
    }
    list.append(element)
    low.append(item['l'])
    high.append(item['h'])


min_value = min(low)
max_value = max(high)


list.append({ 'minOf7Days': min_value, 'maxOf7Days': max_value })

print(min_value)
print(max_value)
df = pandas.DataFrame(list).to_excel(symbol + ".xlsx", index=False)
