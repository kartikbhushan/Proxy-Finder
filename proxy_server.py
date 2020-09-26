import requests
from bs4 import BeautifulSoup
from random import choice
import sys

def get_proxy():
    url = "https://www.sslproxies.org/"
    r = requests.get(url)
    soup = BeautifulSoup(r.content, 'html5lib')
    return {'https': choice(list(map(lambda x:'https://'+x[0]+':'+x[1], list(zip(map(lambda x:x.text, soup.findAll('td')[::8]), 
                                                                      map(lambda x:x.text, soup.findAll('td')[1::8]))))))}

def proxy_request(request_type, url, **kwargs):
    global proxy
    while 1:
        try:
            proxy = get_proxy()
            print("[+] Using Proxy :{}".format(proxy))
            response = requests.request(request_type, url, proxies=proxy, timeout=5, **kwargs)
            break
        except KeyboardInterrupt:
            print("[-] Ctrl + C exiting code")
            sys.exit()
        except Exception as e:
            pass
    return response


r = proxy_request('get', "https://www.youtube.com/")
if r.text != '':
    print("[*][*][*][*][*] Proxy found " + str(proxy))
