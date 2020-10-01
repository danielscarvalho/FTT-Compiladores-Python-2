import requests

resp = requests.get("https://api.duckduckgo.com/?q=Salvador+Arena&format=json&pretty=0")

#print(resp.text)

ddg = resp.json()

print(ddg["Abstract"])

