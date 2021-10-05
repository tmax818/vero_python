import urllib.request, json

with urllib.request.urlopen("https://api.coindesk.com/v1/bpi/currentprice.json") as url:
    data = json.loads(url.read().decode())
    print(data['bpi']['USD']['rate'])