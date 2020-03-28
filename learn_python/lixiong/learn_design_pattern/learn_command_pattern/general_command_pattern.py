

class AbstractCommand:
    # 实现类必须定义一个接收者
    receiver = None

    def execute(self):
        pass


class ConcreteCommand_1(AbstractCommand):

    def execute(self):
        self.receiver.do_something()


class ConcreteCommand_2(AbstractCommand):

    def execute(self):
        self.receiver.do_something()


class Invoker:

    def __init__(self):
        self.command = None

    def set_command(self, command):
        self.command = command

    def action(self):
        self.command.execute()


class Client:

    def run(self):
        invoker = Invoker()
        command = ConcreteCommand_1()
        invoker.set_command(command)
        invoker.action()

