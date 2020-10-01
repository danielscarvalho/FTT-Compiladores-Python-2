import requests

resp = requests.get("https://www.mercadobitcoin.net/api/BTC/ticker")

btc = resp.json()

print(btc)
print(btc["ticker"]["high"], btc["ticker"]["date"])

arquivo = open("bitcoin.tsv","a")
arquivo.write("{}\t{}\n".format(btc["ticker"]["high"], btc["ticker"]["date"]))
arquivo.close()

