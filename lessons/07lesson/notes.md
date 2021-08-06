# VeroSkills

Note:

```python
# while loops

number = 1

while number < 100:
    print(number)
    number += 1
    
print("the number is:",number)

print numbers between 1 and 100 and print even/odd

while number < 100:
    if number % 2 == 0:
        print(number, "is even")
    else:
        print(number, "is odd")
    number += 1
```

```python
import urllib.request, json 
import time

while True:
    with urllib.request.urlopen("https://api.coindesk.com/v1/bpi/currentprice.json") as url:
        data = json.loads(url.read().decode())
        # print(data)
        # print(data['time'])
        # print(data['chartName'])
        print(data['bpi']['USD']['rate'])
    time.sleep(5)
```