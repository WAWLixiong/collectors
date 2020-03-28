# learn: 中介者模式原理类似于网络拓扑的星型结构
# 同事类只处理与自己有关的，与自己无关的交给中介者处理
import random

class AbstractMediator:

    def __init__(self):
        # caution 这里很重要的一点就是要把自己传进去
        # 采购
        self.purchase = Purchase(self)
        # 销售
        self.sale = Sale(self)
        # 库存
        self.stock = Stock(self)

    def execute(self, command:str):
        pass


class Mediator(AbstractMediator):

    def execute(self, command:str=None, number=None, *args, **kwargs):
        if command == 'purchase.buy':
            self.buy_computer(number)
        elif command == 'sale.sell':
            self.sell_computer(number)
        elif command == 'sale.off_sell':
            self.off_sell()
        elif command == 'stock.clear':
            self.clear_stock()

    def buy_computer(self, number):
        sale_status = self.sale.get_sell_status()
        if sale_status > 80:
            self.stock.increase(number)
            print('销售状况良好, 采购{}台'.format(number))
        else:
            buy_number = number // 2
            self.stock.increase(buy_number)
            print('销售状况不好,采购{}台'.format(buy_number))

    def sell_computer(self, number):
        stock_number = self.stock.get_stock_number()
        if stock_number < number:
            self.purchase.buy_computer(number)
        self.stock.decrease(number)

    def off_sell(self):
        print('折价销售所有电脑:{}台'.format(self.stock.get_stock_number()))

    def clear_stock(self):
        self.sale.off_sale()
        self.purchase.refuse_buy_computer()


class AbstractColleague:

    def __init__(self, mediator):
        # 指定中介者是谁，这样就可以维护多个中介者
        self.mediator = mediator


class Purchase(AbstractColleague):

    def buy_computer(self, number):
        self.mediator.execute('purchase.buy', number)

    def refuse_buy_computer(self):
        print('不再采购电脑')


class Sale(AbstractColleague):

    def sell_computer(self, number):
        self.mediator.execute('sale.sell', number)
        print('销售电脑：{}台'.format(number))

    def get_sell_status(self):
        sale_status = random.randint(0, 100)
        print('电脑销售情况为：{}'.format(sale_status))
        return sale_status

    def off_sale(self):
        self.mediator.execute('sale.off_sell')


class Stock(AbstractColleague):
    COMPUTER_NUMBER = 1000

    def increase(self, number):
        self.COMPUTER_NUMBER += number

    def decrease(self, number):
        self.COMPUTER_NUMBER -= number

    def get_stock_number(self):
        return self.COMPUTER_NUMBER

    def clear_stock(self):
        print('清理库存数量为：{}'.format(self.COMPUTER_NUMBER))
        self.mediator.execute('stock.clear')


class Client:

    def run(self):
        mediator = Mediator()
        purchase = Purchase(mediator)
        stock = Stock(mediator)
        sale = Sale(mediator)

        purchase.buy_computer(100)
        sale.sell_computer(1)
        stock.clear_stock()

if __name__ == '__main__':
    client = Client()
    client.run()
    """
    电脑销售情况为：40
    销售状况不好,采购50台
    销售电脑：1台
    清理库存数量为：1000
    折价销售所有电脑:1049台
    不再采购电脑
    """
