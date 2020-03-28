
class Mydict(dict):
    def __setitem__(self, key, value):
        super().__setitem__(key, value*2)


mydict = Mydict(a=1)
print(mydict) #{'a': 1}


from collections import UserDict
class Mydict(UserDict):
    def __setitem__(self, key, value):
        super().__setitem__(key, value*2)


mydict = Mydict(a=1)
print(mydict) #{'a': 1}

mydict['a'] = 1
print(mydict) #{'a': 2}

from collections import defaultdict

mydict = defaultdict(dict)
print(mydict['a'])