a = [1, 6, 3, 2]

def fun(a, b):
    return a - b

b = a.sort(cmp=fun)
print(b)