import requests
import json

r = requests.get(input())
if r.status_code != 200:
    print("Invalid quote resource!")
    print("Invalid quote resource!")
else:
    json_string = r.content
    json_string_content = json.loads(r.content)

    if 'content' not in json_string_content:
        print("Invalid quote resource!")
    else:
        print(json_string_content['content'])

