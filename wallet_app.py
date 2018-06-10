"""
This app helps to control your own finances, your wallet.
    It contains accounts, period of the your money spends,
    transactions with date, value and categories of spends.
    Also it contains functions with count your spends on average.
    App connects to database and makes a manipulation with data, after that returns the data to db.

"""

from datetime import datetime
from decimal import *
from kivy.storage.jsonstore import JsonStore


class AppUnit(object):
    def __init__(self, name, value):
        self.name = name
        self.value = value


class Account(AppUnit):
    # var name always is string, var value is number
    pass


class Transaction(AppUnit):

    # var name always is string, var value is number, account is object of Account class
    def __init__(self, value, account, category):
        super(Transaction, self).__init__(name=datetime.now().strftime("%d-%m-%y %H:%M:%S"), value={'value': value})
        self.value['account'] = account
        self.value['category'] = category


class Category(AppUnit):
    pass


class Wallet(object):
    transaction_list = {}
    account_list = {}
    category_list = {}

    def add_account(self, account):
        save_to_file('accounts.json', account)

    def add_transaction(self, transaction):
        save_to_file('transactions.json', transaction)
        decimal_account = Decimal(self.account_list[transaction.value['account']]).quantize(Decimal('0.01'), rounding=ROUND_DOWN)
        decimal_transaction = Decimal(transaction.value['value']).quantize(Decimal('0.01'), rounding=ROUND_DOWN)
        if self.category_list[transaction.value['category']]:
            result = decimal_account - decimal_transaction
        else:
            result = decimal_account + decimal_transaction
        acc = Account(transaction.value['account'], str(result))
        save_to_file('accounts.json',acc)

    def add_category(self,cat):
        # name is string and value is boolean true for spends and false for incomes
        save_to_file('categories.json', cat)


def list_view(input_dict):
    view_string = ""
    for item in input_dict.items():
        view_string += ('{}:{}\n'.format(item[0], item[1]))
    return view_string + '\n'


def search(input_list):
    total = 0
    total_income = 0
    search_stack = []
    search_stack_income = []
    for item in (input_list.keys()):
        if input_list[item]['category'] in [i for i in wallet.category_list if wallet.category_list[i] is True]:
            search_stack.append('{}:\n{}'.format(item, list_view(input_list[item])))
            total += Decimal(input_list[item]['value']).quantize(Decimal('0.01'), rounding=ROUND_DOWN)
        else:
            search_stack_income.append('{}:\n{}'.format(item, list_view(input_list[item])))
            total_income += Decimal(input_list[item]['value']).quantize(Decimal('0.01'), rounding=ROUND_DOWN)
    balance = total_income-total
    return total, sorted(search_stack,reverse=True), total_income, sorted(search_stack_income, reverse=True),balance


def last_transaction_view(option):
    if option:
        return search(wallet.transaction_list)[1][0]
    else:
        return search(wallet.transaction_list)[3][0]


def save_to_file(file_name, record):
    data_loaded = JsonStore(file_name)
    data_loaded.store_put(record.name,record.value)
    data_loaded.store_sync()
    data_loaded = JsonStore(file_name)

def read_from_file(file_name):
    data_loaded = JsonStore(file_name)
    return data_loaded._data


wallet = Wallet()

wallet.category_list = read_from_file('categories.json')
wallet.transaction_list = read_from_file('transactions.json')
wallet.account_list = read_from_file('accounts.json')


def add_new_tr(acc, cat, val):
    if val:
        wallet.add_transaction(Transaction(val, acc, cat))


def del_tr(mode):
    list = (search(wallet.transaction_list)[mode])
    if len(list) > 1:
        last_tr = (list[0]).split(':\n')[0]
        last_tr = last_tr.split(':\n')[0]
        del wallet.transaction_list[last_tr]
        save_to_file('transactions.json', wallet.transaction_list)


def add_new_acc(acc,val):
    wallet.add_account(Account(acc, val))


def add_new_cat(name,val):
    wallet.add_category(Category(name, val))


def del_cat(cat):
    del(wallet.category_list[cat])
    save_to_file('categories.json', wallet.category_list)


def del_acc(acc):
    if wallet.account_list:
        del(wallet.account_list[acc])
        save_to_file('accounts.json', wallet.account_list)
    else:
        wallet.account_list['cash'] = 0
        save_to_file('accounts.json', wallet.account_list)