import requests
import json

user_currency = input()

r = requests.get(f'http://www.floatrates.com/daily/{user_currency.lower()}.json')
json_string = r.content
json_string_object = json.loads(json_string)


new_dict = {}

while True:
    needed_currency = input().lower()
    print(new_dict)


    if needed_currency == "":
        break
    amount = float(input())
    if needed_currency.upper() == 'USD':
        usd_fixed = json_string_object['usd']
        new_dict = {usd_fixed['code']: usd_fixed['rate']}
        print("Checking the cache...")
        print("Oh! It is in the cache!")
        print(f"You received {round(amount * usd_fixed['rate'], 2)} USD.")
        continue
    elif needed_currency.upper() == 'EUR':
        eur_fixed = json_string_object['eur']
        new_dict = {eur_fixed['code']: eur_fixed['rate']}
        print("Checking the cache...")
        print("Oh! It is in the cache!")
        print(f"You received {round(amount * eur_fixed['rate'], 2)} EUR.")
        continue
    elif needed_currency.upper() in new_dict.keys():
        for i in new_dict.keys():
            if i == needed_currency:
                print(i.value())
        print("Checking the cache...")
        print("Oh! It is in the cache!")
        print(f"You received {round(amount * i.value(), 2)} {needed_currency.upper()}.")
        
        continue
    else:
        json_needed_currency = json_string_object[needed_currency]
        new_dict[json_needed_currency['code']] = json_needed_currency['rate']
        print("Checking the cache...")
        print("Sorry, but it is not in the cache!")
        print(f"You received {round(amount * json_needed_currency['rate'], 2)} {needed_currency.upper()}.")
        continue
    print(new_dict)









