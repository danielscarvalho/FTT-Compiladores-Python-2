# Instalar a biblioteca externa requets:
# pip install requests
# ou
# pip3 install requests

# https://pypi.org/project/requests/
# https://requests.readthedocs.io/en/master/


import requests

resp = requests.get("http://ftt.com.br/home/")

print(resp.text)
