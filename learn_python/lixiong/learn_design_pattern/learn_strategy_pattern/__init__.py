
class Strategy:

    def do_something(self):
        pass

class ConcreteStrategy_1(Strategy):

    def do_something(self):
        print('1')


class ConcreteStrategy_2(Strategy):

    def do_something(self):
        print('2')


class Context:

    def __init__(self, stategy):
        self.stategy = stategy

    def do_any_thing(self):
        self.stategy.do_something()


class Client:

    def run(self):
        strategy = ConcreteStrategy_1()
        context = Context(stategy=strategy)
        context.do_any_thing()

# learn: 策略枚举


class Calculatot:

    class ADD:

        def exec(self, a, b):
            return a + b

    class SUB:

        def exec(self, a, b):
            return a - b

    def __init__(self, value):
        self.value = value

    def get_value(self):
        return self.value

    def exec(self, a, b):
        pass


class Client_2:

    def run(self):

        a =  int(input())
        b = int(input())
        symbol = input()
        