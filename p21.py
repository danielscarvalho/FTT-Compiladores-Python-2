import requests


#print(resp.text)


while True:
    query = input("O que vc quer saber: ")
    if len(query) == 0:
        break

    resp = requests.get("https://api.duckduckgo.com/?format=json&pretty=0&q=" + query)

    ddg = resp.json()
    print(ddg["Abstract"])
    print()

