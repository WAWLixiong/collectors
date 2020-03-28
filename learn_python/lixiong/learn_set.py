
a = set('abcd')
print(a)

b = frozenset()
print(b)

c = frozenset('abcd')  #由于不可变，可以作为dict的键
print(c)


d = set()


#字典的内存占用率比较大，但是查询速度快，自定义的对象，或者python内部的对象都是dict包装的
#字典的顺序与插入字典的顺序有关系
#插入数据可能会重新排列顺序
#字典的键和集合的值都必须是可以hash的


