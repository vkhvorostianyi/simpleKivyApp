"""
This app helps to control your own finances, your wallet.
    It contains accounts, period of the your money spends,
    transactions with date, value and categories of spends.
    Also it contains functions with count your spends on average.
    App connects to database and makes a manipulation with data, after that returns the data to db.

"""

from datetime import datetime
from decimal import *
import json


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
        super(Transaction,self).__init__(name=datetime.now().strftime("%d-%m-%y %H:%M:%S"), value=value)
        self.name = datetime.now().strftime("%d-%m-%y %H:%M:%S")
        self.account = account
        self.category = category


class Category(AppUnit):
    pass


class Wallet(object):
    transaction_list = {}
    account_list = {}
    category_list = {}

    def add_account(self, account):
        self.account_list[account.name] = str(account.value)
        save_to_file('accounts.json', self.account_list)

    def add_transaction(self, transaction):
        tr_cell = self.transaction_list[transaction.name] = {}
        tr_cell["category"] = transaction.category
        tr_cell["value"] = transaction.value
        tr_cell['account'] = transaction.account
        save_to_file('transactions.json', self.transaction_list)
        decimal_account = round(float(self.account_list[transaction.account]), 2)
        decimal_transaction = round(float(transaction.value), 2)
        if self.category_list[transaction.category]:
            result = decimal_account - decimal_transaction
        else:
            result = decimal_account + decimal_transaction
        self.account_list[transaction.account] = str(result)
        save_to_file('accounts.json', self.account_list)

    def add_category(self,cat):
        # name is string and value is boolean true for spends and false for incomes
        self.category_list[cat.name] = cat.value
        save_to_file('categories.json', self.category_list)


def list_view(input_dict):
    view_string = ""
    for item in input_dict.items():
        view_string += ('{}:{}\n'.format(item[0], item[1]))
    return view_string + '\n'


def search(input_list, keyword=None):
    total = 0
    total_income = 0
    search_stack = []
    search_stack_income = []
    if keyword:
        for item in (input_list.keys()):
            if keyword in (item and str(input_list[item].values())):
                search_stack.append('{}:\n{}'.format(item, list_view(input_list[item])))
                total += round(float(input_list[item]['value']), 2)
        else:
            if search_stack:
                for i in search_stack:
                    print(i)
                return total, sorted(search_stack)
            else:
                return "No results,sorry"
    else:
        for item in (input_list.keys()):
            if input_list[item]['category'] in [i for i in wallet.category_list if wallet.category_list[i] is True]:
                search_stack.append('{}:\n{}'.format(item, list_view(input_list[item])))
                total += round(float(input_list[item]['value']), 2)
            else:
                search_stack_income.append('{}:\n{}'.format(item, list_view(input_list[item])))
                total_income += round(float(input_list[item]['value']), 2)
        balance = total_income-total
        return total, sorted(search_stack,reverse=True), total_income, sorted(search_stack_income, reverse=True),balance


def last_transaction_view(option):
    if option:
        return search(wallet.transaction_list)[1][0]
    else:
        return search(wallet.transaction_list)[3][0]


def save_to_file(file_name, data):
    with open(file_name, "w") as outfile:
        json.dump(data, outfile)


def read_from_file(file_name):
    with open(file_name) as data_file:
        data_loaded = json.load(data_file)
    return data_loaded


wallet = Wallet()

wallet.category_list = read_from_file('categories.json')
wallet.transaction_list = read_from_file('transactions.json')
wallet.account_list = read_from_file('accounts.json')

if not wallet.account_list:
    wallet.account_list['cash(default)'] = '0.00'
if not wallet.category_list:
    wallet.category_list['transport(default)'] = True
if not wallet.transaction_list:
    time = datetime.now().strftime("%d-%m-%y %H:%M:%S")
    wallet.transaction_list[time]={'value':'0.00','account':None,'category': None}


def add_new_tr(acc, cat, val):
    if val:
        wallet.add_transaction(Transaction(val, acc, cat))


def add_new_acc(acc,val):
    wallet.add_account(Account(acc, val))


def add_new_cat(name,val):
    wallet.add_category(Category(name, val))


def del_cat(cat):
    del(wallet.category_list[cat])
    save_to_file('categories.json', wallet.category_list)


def del_acc(acc):
    del(wallet.account_list[acc])
    save_to_file('accounts.json', wallet.account_list)