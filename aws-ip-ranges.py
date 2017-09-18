import requests
import json

url = 'https://ip-ranges.amazonaws.com/ip-ranges.json'
response = requests.get(url)
jsonObject = json.loads(response.content)

for item in jsonObject["prefixes"]:
    print item["ip_prefix"], item["region"]

#    print item["ip_prefix"], item["region"]
