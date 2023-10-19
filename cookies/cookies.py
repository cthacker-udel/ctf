import requests
from time import sleep


with open('explored_cookies.txt', 'a') as cookie_file:
    with open('output.txt', 'w') as f:
        for i in range(0, 100):
            try:
                print('testing cookie ', i)
                s = requests.Session()
                s.cookies.set("name", f'{i}')
                x = s.request("GET",'http://mercury.picoctf.net:54219/check' )
                f.write(x.text)
                sleep(1)
                cookie_file.write(f'{i} ')
            except:
                pass