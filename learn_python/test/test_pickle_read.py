import pickle

with open('pickle_sample', 'br') as f:
    a = pickle.load(f)

print(type(a))
print(a.name)
