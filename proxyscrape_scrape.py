import urllib.request
import requests

timeout = 10000 #put your own timeout here

proxytype = ["http","socks4","socks5"]
for x in proxytype:
    proxies = requests.get('https://api.proxyscrape.com?request=amountproxies&proxytype={}'.format(x))
    url = 'https://api.proxyscrape.com?request=getproxies&proxytype={}&timeout={}'.format(x,timeout)
    print('Scraping '+ proxies.text +'\t' + x + ' proxies...')
    urllib.request.urlretrieve(url, '{}.txt'.format(x))