import requests
import json

user_currency = input()
expected_currency = input()
user_budget = float(input())

r = requests.get(f'http://www.floatrates.com/daily/{user_currency.lower()}.json')
json_string = r.content
json_string_object = json.loads(json_string)


