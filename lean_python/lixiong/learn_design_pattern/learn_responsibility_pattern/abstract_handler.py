# 在实际的应用中，一般会有一个封装类对责任模式进行封装，代替Client类，直接返回链中的第一个处理者
class AbstractHandler:

    next_handler = None

    def handle_message(self, request):
        response = None
        if self.get_handle_level() == request.get_request_level():
            response = self.response()
        else:
            if self.next_handler is not None:
                response = self.next_handler.handle_message(request)
        return response

    def get_handle_level(self):
        pass

    def set_next_handle(self, handle):
        self.next_handler = handle

    def response(self):
        pass


class ConcreteHandler_1(AbstractHandler):

    def response(self):
        return 'i am 1'

    def get_handle_level(self):
        return 1


class ConcreteHandler_2(AbstractHandler):

    def response(self):
        return 'i am 2'

    def get_handle_level(self):
        return 2


class Request1:

    def get_request_level(self):
        return 2


class Client:

    def run(self):
        handler_1 = ConcreteHandler_1()
        handler_2 = ConcreteHandler_2()
        handler_1.set_next_handle(handler_2)
        request_1 = Request1()
        ret = handler_1.handle_message(request_1)
        return ret

if __name__ == '__main__':
    client = Client()
    ret = client.run()
    print(ret)
