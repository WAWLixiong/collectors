import pickle

class A:
    def __init__(self, name):
        self.name = name
        print('my name is {}'.format(self.name))


def test_write():
    a = A('zzlion')
    with open('pickle_sample', 'bw') as f:
        pickle.dump(a, f)