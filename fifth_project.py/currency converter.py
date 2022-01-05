import requests
import json
import requests
import json

user_currency = input()

r = requests.get(f'http://www.floatrates.com/daily/{user_currency.lower()}.json')
json_string = r.content
json_string_object = json.loads(json_string)

usd_fixed = requests.get(f'http://www.floatrates.com/daily/usd.json')
eur_fixed = requests.get(f'http://www.floatrates.com/daily/eur.json')

new_dict = {}
new_dict = {usd_fixed['code']: usd_fixed['rate'], eur_fixed['code']: eur_fixed['rate']}
print(new_dict)

while True:
    needed_currency = input().lower()

    if needed_currency == "":
        break
    amount = float(input())
    # if needed_currency.upper() == 'USD':
    #     print("Checking the cache...")
    #     print("Oh! It is in the cache!")
    #     print(f"You received {round(amount * usd_fixed['rate'], 2)} USD.")
    #     continue
    # elif needed_currency.upper() == 'EUR':
    #     print("Checking the cache...")
    #     print("Oh! It is in the cache!")
    #     print(f"You received {round(amount * eur_fixed['rate'], 2)} EUR.")
    #     continue
    if needed_currency.upper() in new_dict.keys():
        print("Checking the cache...")
        print("Oh! It is in the cache!")
        print(f"You received {round(amount * json_needed_currency['rate'], 2)} {needed_currency.upper()}.")
        continue
    else:
        json_needed_currency = json_string_object[needed_currency]
        new_dict[json_needed_currency['code']] = json_needed_currency['rate']
        print("Checking the cache...")
        print("Sorry, but it is not in the cache!")
        print(f"You received {round(amount * json_needed_currency['rate'], 2)} {needed_currency.upper()}.")
        continue






