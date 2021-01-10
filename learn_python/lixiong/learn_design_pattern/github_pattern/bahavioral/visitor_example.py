#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2020/7/21 下午 10:00:18
# @Author  : zzlion
# @File    : visitor_example.py
# @Reference:


class Finance:
    """财务数据结构类"""

    def __init__(self):
        self.salesvolume = None  # 销售额
        self.cost = None  # 成本
        self.history_salesvolume = None  # 历史销售额
        self.history_cost = None  # 历史成本

    def set_salesvolume(self, value):
        self.salesvolume = value

    def set_cost(self, value):
        self.cost = value

    def set_history_salesvolume(self, value):
        self.history_salesvolume = value

    def set_history_cost(self, value):
        self.history_cost = value

    def accept(self,):
        pass


class Finance_year(Finance):
    """2018年财务数据类"""

    def __init__(self, year):
        super().__init__()
        self.workers = []  # 安排工作人员列表
        self.year = year

    def add_worker(self, worker):
        self.workers.append(worker)

    def accept(self):
        for obj in self.workers:
            obj.visit(self)


class Accounting:
    """会计类"""

    def __init__(self):
        self.id_ = '会计'
        self.duty = '计算报表'

    def visit(self, table):
        print('会计年度: {}'.format(table.year))
        print('我的身份是: {} 职责: {}'.format(self.id_, self.duty))
        print('本年度纯利润: {}'.format(table.salesvolume - table.cost))
        print('-' * 50)


class Audit:
    """财务总监类"""

    def __init__(self):
        self.id_ = '财务总监'
        self.duty = '分析业绩'

    def visit(self, table):
        print('会计总监年度： {}'.format(table.year))
        print("我的身份是： {} 职责： {}".format(self.id_, self.duty))
        if table.salesvolume - table.cost > table.history_salesvolume - table.history_cost:
            msg = "较同期上涨"
        else:
            msg = "较同期下跌"
        print('本年度公司业绩： {}'.format(msg))
        print('------------------')


class Adviser:
    """战略顾问"""

    def __init__(self):
        self.id_ = "战略顾问"
        self.duty = "制定明年战略"

    def visit(self, table):
        print('战略顾问年度： {}'.format(table.year))
        print("我的身份是： {} 职责： {}".format(self.id_, self.duty))
        if table.salesvolume > table.history_salesvolume:
            msg = "行业上行，扩大生产规模"
        else:
            msg = "行业下行，减小生产规模"
        print('本年度公司业绩： {}'.format(msg))
        print('------------------')


class Work:
    """工作类"""

    def __init__(self):
        self.works = [] # 需要处理的年度数据列表

    def add_work(self, obj):
        self.works.append(obj)

    def remove_work(self, obj):
        self.works.remove(obj)

    def visit(self):
        for obj in self.works:
            obj.accept()


if __name__ == '__main__':
    work = Work()

    finance_2018 = Finance_year(2018)
    finance_2018.set_salesvolume(200)
    finance_2018.set_cost(100)
    finance_2018.set_history_salesvolume(180)
    finance_2018.set_history_cost(90)

    accounting = Accounting()
    audit = Audit()
    adviser = Adviser()

    finance_2018.add_worker(accounting)
    finance_2018.add_worker(audit)
    finance_2018.add_worker(adviser)

    work.add_work(finance_2018)
    work.visit()
