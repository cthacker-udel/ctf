import requests

session = requests.Session()
session.cookies.set('name', 9)

for i in range(1, 10):
    x = requests.get('http://mercury.picoctf.net:54219/check', cookies={
        'name': i
    })
    print(x)