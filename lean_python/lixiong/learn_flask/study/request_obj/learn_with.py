import traceback

class A:

    def __init__(self, name):
        self.name = name

    def __enter__(self):
        self.name = self.name.upper()


    def __exit__(self, exc_type, exc_val, exc_tb):
        print(exc_tb)
        print(exc_type)
        print(exc_val)


with A(name='zz') as f:
    try:
        print(f.name)
    except Exception as e:
        print(traceback.format_exc())


print('hi')

