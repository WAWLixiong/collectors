a = [1, 2, 3, 4, 5, 6, 7]

print(a[::])
print(a[:])
print(a[::-1])
print(a[:3:-1])
print(a[::2])
print(a[:4:2])

a[:3] = []
print(a)

a[::2] = [8]*2
print(a)

a[:2] = [9]*2
print(a)

a[2:2] = [10,11]
print(a)

a[len(a):] = [12,12]
print(a)

