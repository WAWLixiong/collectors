import requests
from collections import abc
from _collections_abc import __all__
url = 'http://www.baidu.com'

resp = requests.get(url)


a = [1,2]
a += (1,2)
print(a)

a = a + [1,2]
a = a + (1,2)
print(a)
