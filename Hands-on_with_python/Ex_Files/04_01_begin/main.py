import json
from pprint import pprint
import requests

response = requests.get(
    "http://api.worldbank.org/v2/countries/USA/indicators/SP.POP.TOTL?per_page=5000&format=json")

last_twenty_years = response.json()[1][:20]

for i in last_twenty_years:
    #pprint(json.dumps(i))
    display=i["value"]// 10_000_000
    print(f'date {i["date"]}: {i["value"]// 10_000_000}', "=" * display)