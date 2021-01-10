#Sequence
import numbers


class Group:
    def __init__(self, group_name, company_name, staffs):
        self.group_name = group_name
        self.company_name = company_name
        self.staffs = staffs

    def __reversed__(self):
        self.staffs.reverse()

    def __getitem__(self, item):
        cls = type(self)
        if isinstance(item, slice):
            return cls(group_name=self.group_name, company_name=self.company_name,staffs=self.staffs[item])
        elif isinstance(item,numbers.Integral):
            return cls(group_name=self.group_name, company_name=self.company_name,staffs=[self.staffs[item]])

    def __len__(self):
        return len(self.staffs)

    def __iter__(self):
        pass

    def __contains__(self, item):
        if item in self.staffs:
            return True
        return False


if __name__ == '__main__':
    group = Group(company_name='imooc', group_name='user', staffs=['zzlion','mooc','lili'])
    reversed(group)
    print(group.staffs)
    staffs_group = group[:2] #不会报错，主要是由于事先了getitem方法
    group[0]
    if 'zzlion' in group:
        print('yes')
    pass
