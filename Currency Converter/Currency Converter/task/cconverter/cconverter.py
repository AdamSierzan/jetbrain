import requests
import json
currency = input()
r = requests.get(f'http://www.floatrates.com/daily/{currency.lower()}.json')
json_string = r.content
json_string_object = json.loads(json_string)
print(json_string_object['usd'])
print(json_string_object['eur'])

