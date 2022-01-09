import requests
import json
import requests
import json

user_currency = input()

r = requests.get(f'http://www.floatrates.com/daily/{user_currency.lower()}.json')
json_string = r.content
json_string_obejct = json.loads(json_string)
usd = json_string_obejct['usd']
eur = json_string_obejct['eur']

new_dict = {usd['code']: usd['rate']}
new_dict[eur['code']] = eur['rate']
while True:
    needed_currency = input().lower()
    if needed_currency == "":
        break
    amount = float(input())
    if needed_currency == 'USD':
        print("Checking the cache...")
        print("Oh! It is in the cache!")
        print(f"You received {round(amount*usd['rate'], 2)} USD.")
        continue
    elif needed_currency == 'EUR':
        print("Checking the cache...")
        print("Oh! It is in the cache!")
        print(f"You received {round(amount*eur['rate'], 2)} EUR.")
        continue
    elif needed_currency.upper() in new_dict.keys():
        print("Checking the cache...")
        print("Oh! It is in the cache!")
        print(f"You received {round(amount*json_needed_currency['rate'], 2)} {needed_currency.upper()}.")
        continue
    else:
        json_needed_currency = json_string_obejct[needed_currency]
        new_dict[json_needed_currency['code']] = json_needed_currency['rate']
        print("Checking the cache...")
        print("Sorry, but it is not in the cache!")
        print(f"You received {round(amount*json_needed_currency['rate'], 2)} {needed_currency.upper()}.")
        continue







