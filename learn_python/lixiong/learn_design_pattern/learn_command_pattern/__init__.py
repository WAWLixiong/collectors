# 类间解耦，调用角色与接收角色之间没有依赖关系，调用者实现功能时只需调用Command抽象类的execute即可
# 可扩展性，Command可以随意扩展
class AbstractCommand:

    def __init__(self):
        self.rg = RequirementGroup()
        self.pg = PageGroup()
        self.cg = CodeGroup()

    def execute(self):
        pass


class AddRequirementCommand(AbstractCommand):

    def execute(self):
        self.rg.find()
        self.rg.add()
        self.rg.plan()


class DeletePageCommand(AbstractCommand):

    def execute(self):
        self.pg.find()
        self.rg.delete()
        self.rg.plan()


class CancelDeletePageCommand(AbstractCommand):

    def execute(self):
        self.pg.roll_back()


class Invoker:

    def __init__(self):
        self.command = None

    def set_command(self, command):
        self.command = command

    def action(self):
        self.command.execute()


class AbstractGroup:

    def find(self):
        pass

    def add(self):
        pass

    def delete(self):
        pass

    def change(self):
        pass

    def plan(self):
        pass

    def roll_back(self):
        pass


class RequirementGroup(AbstractGroup):

    def find(self):
        print('找到需求组')

    def add(self):
        print('客户要求增加一项需求')

    def change(self):
        print('客户要求修改一项功能')

    def delete(self):
        print('客户要求删除一项功能')

    def plan(self):
        print('客户要求需求变更计划')


class PageGroup(AbstractGroup):

    def find(self):
        print('找到美工组')

    def add(self):
        print('客户要求增加一个页面')

    def change(self):
        print('客户要求修改一个页面')

    def delete(self):
        print('客户要求删除一个页面')

    def plan(self):
        print('客户要求页面变更计划')


class CodeGroup(AbstractGroup):

    def find(self):
        print('找到代码组')

    def add(self):
        print('客户要求增加一项功能')

    def change(self):
        print('客户要求修改一项功能')

    def delete(self):
        print('客户要求删除一项功能')

    def plan(self):
        print('客户要求代码变更计划')


class Client:

    def run(self):
        xiao_gang = Invoker()
        command = AddRequirementCommand()
        xiao_gang.set_command(command)
        xiao_gang.action()
