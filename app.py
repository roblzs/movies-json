import requests
import json

url = 'https://www.swapi.tech/api/films'

data = {}

for i in range(6):
    i += 1

    key = f"film{i}"

    req_url = f"{url}/{i}"

    res = requests.get(req_url)
    res_json = res.json()

    data[key] = res_json["result"]

json_write = json.dumps(data, ensure_ascii=False, indent=4)

with open('data.json', 'w', encoding='utf-8') as f:
    f.write(json_write)
