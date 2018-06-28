import pickle
from datetime import datetime
from decimal import Decimal, ROUND_DOWN


class Base(object):

    def __init__(self, name, value):
        self.name = name
        self.value = value
        self.code = None

    def decimalize(self):
        self.value = Decimal(self.value).quantize(Decimal('0.01'), rounding=ROUND_DOWN)

    def record(self):
        log[self.code][self.name] = self

    def __repr__(self):
        s = f'<name:{self.name}, value: {self.value}>'
        return s


class Account(Base):

    def __init__(self, name, value):
        super().__init__(name, 0)
        self.code = 0
        self.decimalize()
        Transaction(value, self, category=Category('init_new_account', False))
        self.record()


class Category(Base):
    def __init__(self, name, value):
        super().__init__(name, value)
        self.code = 1
        self.record()


class Transaction(Base):

    def __init__(self, value, account, category):
        super().__init__(name=datetime.now().strftime("%d-%m-%y %H:%M:%S"), value=value)
        self.account = account
        self.category = category
        self.make_spend()
        self.decimalize()
        self.code = 2
        self.record()

    def make_spend(self):
        if self.category.value:
            self.account.value = self.account.value - self.value
        else:
            self.account.value = self.account.value + self.value


def balance_count():
    sum_income = sum([x.value for x in log[2].values() if not x.category.value])
    sum_outcome = sum([x.value for x in log[2].values() if x.category.value])
    balance = sum_income - sum_outcome
    return balance


def account_parse(code):
    data = []
    
    if code == 0 and log[code]:
        data = ['{}:{}\n'.format(x.name, x.value) for x in log[0].values()]
    
    elif code == 1 and log[code]:
        data = ['{}\n'.format(x.name) for x in log[1].values()]

    elif code == 2 and log[code]:
        data = ['{}\n{}\n{}\{}\n\n'.format(x.name, x.value, x.category.name, x.account.name) for x in log[2].values()]
    
    return data


def dump_data():
    with open('log.obj', 'wb') as file:
        pickle.dump(log, file)


def load_data():
    with open('log.obj', 'rb') as file:
        return pickle.load(file)


log = load_data()

if not log:
    log = [{}, {}, {}]
