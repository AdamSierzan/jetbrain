import requests
import json
import requests
import json

user_currency = input()
needed_currency = input().lower()
amount = float(input())

r = requests.get(f'http://www.floatrates.com/daily/{user_currency.lower()}.json')
json_string = r.content
json_string_obejct = json.loads(json_string)
usd = json_string_obejct['usd']
eur = json_string_obejct['eur']

new_dict = {usd['code']:usd['rate']}
new_dict[eur['code']] = eur['rate']
print(new_dict)

if needed_currency == 'USD':
    print("Oh! It is in the cache!")
    print(f"You will receive {round(amount*usd['rate'], 2)} USD")
elif needed_currency == 'EUR':
    print("Oh! It is in the cache!")
    print(f"You will receive {round(amount*eur['rate'], 2)} EUR")
else:
    json_needed_currency = json_string_obejct[needed_currency]
    # json_needed_currency_rate = json_needed_currency['rate']
    print("Oh! It's not in the cache!")
    print(f"You will receive {round(amount*json_needed_currency['rate'], 2)} ILS")
    new_dict[json_needed_currency['code']] = json_needed_currency['rate']
print(new_dict)








