# 定义一个
# 复习属性描述符
import numbers


class Fields:
    pass

class IntField(Fields):
    """注意一下init的参数检查与set的参数检查是不一样的，set是设置值时候的参数检查"""

    def __init__(self, db_column, min_value, max_value):
        self._value = None
        self.db_column = db_column
        self.min_value = min_value
        self.max_value = max_value
        if self.min_value:
            if not isinstance(self.min_value, numbers.Integral):
                raise ValueError('min_value must be int')
            elif self.min_value < 0:
                raise ValueError('min_value need positive')
        if self.max_value:
            if not isinstance(self.max_value, numbers.Integral):
                raise ValueError('min_value must be int')
            elif self.max_value < 0:
                raise ValueError('min_value need positive')
        if self.min_value and self.max_value:
            if min_value > max_value:
                raise ValueError('min_value must be smaller than max_value')

    def __get__(self, instance, owner):
        return self._value

    def __set__(self, instance, value):
        if not isinstance(value, numbers.Integral):
            raise ValueError('int value need')
        if not (self.min_value < value < self.max_value):
            raise ValueError('value must between {} and {}'.format(self.min_value, self.max_value))
        self._value = value


class CharField(Fields):
    def __init__(self, max_length, db_column):
        self._value = None
        self.db_column = db_column
        self.max_length = max_length
        if not self.max_length:
            raise ValueError('you must specify max_length for charfield')

    def __get__(self, instance, owner):
        return self._value

    def __set__(self, instance, value):
        if not isinstance(value, str):
            raise ValueError('string value need')
        if len(value) > self.max_length:
            raise ValueError('value must less than {}'.format(self.max_length))
        self._value = value


class MetaClass(type):
    def __new__(cls, name, bases, attrs, **kwargs):
        if name == 'BaseModel':
            return super().__new__(cls, name, bases, attrs, **kwargs) #由于BaseClass调用父类的init方法，所有来到这个地方，并且使用type类来创建对象类
        fields = {}
        for key, value in attrs.items():
            if isinstance(value, Fields):
                fields[key] = value
        attrs_meta = attrs.get("Meta", None)
        _meta = {}
        db_tale = name.lower()
        if attrs_meta:
            table = getattr(attrs_meta, 'db_table')
            if table:
                db_tale = table
        _meta['db_table'] = db_tale
        attrs['_meta'] = _meta
        attrs['fields'] = fields
        del attrs['Meta']
        return super().__new__(cls, name, bases, attrs, **kwargs)


class BaseModel(metaclass=MetaClass):
    def __init__(self, *args, **kwargs):
        for key, value in kwargs.items():
            setattr(self, key, value)
        return super().__init__()

    def save(self):
        fields = []
        values = []
        for key, value in self.fields.items():
            db_column = value.db_column
            if db_column:
                db_column = db_column.lower()
            fields.append(db_column)
            value = getattr(self, key)
            values.append(str(value))
        sql = "insert {} ({}) value ({})".format(self._meta['db_table'], ','.join(fields), ','.join(values))
        print(sql)


class User(BaseModel):
    name = CharField(db_column='name', max_length=10)
    age = IntField(db_column='age', min_value=0, max_value=100)

    class Meta:
        db_table = "user"



if __name__ == '__main__':
    # user = User()
    user = User(name='Lixong', age=18)
    # user.name = 'Lixiong'
    # user.age = 18
    print(user.name)
    print(user.age)
    user.save()
