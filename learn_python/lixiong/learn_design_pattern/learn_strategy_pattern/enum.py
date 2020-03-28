from enum import Enum, unique

@unique
class TaxType(Enum):
    CN_TAX = 0
    US_TAX = 1
    DE_TAX = 2

print(TaxType.CN_TAX)


class SalesOrder:

    # 违背了开闭原则
    def calculate_tax(self, tax_type):
        if tax_type == TaxType.CN_TAX:
            self.cal_cn_tax()
        elif tax_type == TaxType.US_TAX:
            self.cal_us_tax()
        elif tax_type == TaxType.DE_TAX:
            self.cal_de_tax()

    def cal_cn_tax(self):
        print('cal_cn_tax')

    def cal_us_tax(self):
        print('cal_us_tax')

    def cal_de_tax(self):
        print('cal_de_tax')


# 策略模式实现