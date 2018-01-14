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


class Account(object):
    # var name always is string, var value is number
    def __init__(self, name, value):
        self.account_name = name
        self.account_value = value


class Transaction(object):

    # var name always is string, var value is number, account is object of Account class
    def __init__(self, value, account, category):
        self.transaction_name = datetime.now().strftime("%d-%m-%y %H:%M:%S")
        self.transaction_value = value
        self.transaction_account = account
        self.category = category


class Category(object):

    # name is string and is_spend is boolean
    def __init__(self, name, is_spend):
        self.name = name
        self.is_spend = is_spend


class Wallet(object):
    transaction_list = {}
    account_list = {}
    category_list = {}

    def add_account(self, account):
        self.account_list[account.account_name] = str(account.account_value)

    def add_transaction(self, transaction):
        tr_cell = self.transaction_list[transaction.transaction_name] = {}
        tr_cell["value"] = str(transaction.transaction_value)
        tr_cell["category"] = transaction.category
        tr_cell['account'] = transaction.transaction_account


def spend(account, transaction):
    decimal_account = Decimal(account).quantize(Decimal('0.01'), rounding=ROUND_DOWN)
    decimal_transaction = Decimal(transaction).quantize(Decimal('0.01'), rounding=ROUND_DOWN)
    return str(decimal_account - decimal_transaction)


def list_view(input_dict):
    view_string = ""
    for item in input_dict.items():
        view_string += ('{}:{}\n'.format(item[0], item[1]))
    return view_string + '\n'


def search(input_list, keyword=None):
    total = 0
    search_stack = []
    if keyword:
        for item in sorted(input_list.keys(), reverse=True):
            if keyword in (item and str(input_list[item].values())):
                search_stack.append('{}:\n{}'.format(item, list_view(input_list[item])))
                total += Decimal(input_list[item]['value']).quantize(Decimal('0.01'), rounding=ROUND_DOWN)
        else:
            if search_stack:
                for i in search_stack:
                    print(i)
                return total, search_stack
            else:
                return "No results,sorry"
    else:
        for item in sorted(input_list.keys(), reverse=True):
            search_stack.append('{}:\n{}'.format(item, list_view(input_list[item])))
            total += Decimal(input_list[item]['value']).quantize(Decimal('0.01'), rounding=ROUND_DOWN)
        return total, search_stack


def last_transaction_view():
    return search(wallet.transaction_list)[1][0]


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

ac_list = list(wallet.account_list.keys())
print(ac_list)