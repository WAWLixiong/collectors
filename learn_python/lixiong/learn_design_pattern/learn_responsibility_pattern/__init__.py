import random

class AbstractHandler:
    FATHER_LEVEL_REQUEST = 1
    HUSBAND_LEVEL_REQUEST = 2
    SON_LEVEL_REQUEST = 3
    next_handler = None

    level = 0

    def handle_message(self, woman):
        if woman.get_type() == self.level:
            self.response(woman)
        else:
            if self.next_handler is not None:
                self.next_handler.handle_message(woman)
            else:
                print('--没地方请示了，按不同意处理')

    def set_next(self, handler):
        self.next_handler = handler

    def response(self, woman):
        pass


class Father(AbstractHandler):

    level = AbstractHandler.FATHER_LEVEL_REQUEST

    def response(self, woman):
        print('--女儿像父亲请示--')
        print(woman.get_request())
        print('父亲的回答是：同意')


class Husband(AbstractHandler):

    level = AbstractHandler.HUSBAND_LEVEL_REQUEST

    def response(self, woman):
        print('--妻子向丈夫请示--')
        print(woman.get_request())
        print('丈夫的回答是：同意')


class Son(AbstractHandler):

    level = AbstractHandler.SON_LEVEL_REQUEST

    def response(self, woman):
        print('--妻子向儿子请示--')
        print(woman.get_request())
        print('儿子的回答是：同意')


class IWoman:

    def get_type(self):
        pass

    def get_request(self):
        pass

class Woman(IWoman):

    woman_type = 0
    request = ''

    def __init__(self, woman_type, request):
        self.woman_type = woman_type
        if self.woman_type == 1:
            self.request = '女儿的请求是：{}'.format(request)
        elif self.woman_type == 2:
            self.request = '妻子的请求是：{}'.format(request)
        elif self.woman_type == 3:
            self.request = '母亲的请求是：{}'.format(request)

    def get_type(self):
        return self.woman_type

    def get_request(self):
        return self.request


class Client:

    def run(self):
        arry_list = []
        i = 0
        while True:
            if i == 5:
                break
            i += 1
            arry_list.append(Woman(random.randint(1, 3), '我要出去逛街'))
        father = Father()
        husband = Husband()
        son = Son()
        father.set_next(husband)
        husband.set_next(son)
        for i in arry_list:
            father.handle_message(woman=i)

if __name__ == '__main__':
    client = Client()
    client.run()

