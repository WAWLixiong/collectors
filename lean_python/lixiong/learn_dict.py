#dict并不是继承了mutabmapping类，而是实现了mutablemapping的一些特定方法

a = {'student1':{'name':'zzlion'},
     'student2':{'name':'xiaoli'}}

print(a)
# a.clear()
# print(a)

print(a.setdefault('xiongxiong', 'hi'))
print(a.setdefault('student1','wawa'))
print(a.get('hello'))

a.update(a=1,b=2)
print(a)

a.update([('a',2),('b',3)])
print(a)

