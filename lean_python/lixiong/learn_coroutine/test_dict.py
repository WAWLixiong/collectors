
class A:
    name = 'zzlion'


if __name__ == '__main__':
    a = A()
    print(a.name)
    a.name = 'lixiong'
    print(A.name)
    print(A.__dict__)
    print(a.__dict__)
    # zzlion
    # zzlion
    # {'__module__': '__main__', 'name': 'zzlion', '__dict__': <attribute '__dict__' of 'A' objects>, '__weakref__': <attribute '__weakref__' of 'A' objects>, '__doc__': None}
    {'name': 'lixiong'}

