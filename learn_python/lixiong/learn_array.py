import array

#array和list的重要区别，array只能存放指定类型的数据
#array使用连续的内存空间，效率更高

my_array = array.array('i')

my_array.append(12)
my_array.append('a')