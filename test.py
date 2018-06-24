import unittest
from core import *
import time


class TestCase(unittest.TestCase):

    """It is a set of unit-tests for core.py objects"""

    def setUp(self):
        Account('test_ac', 100)
        Category('test_cat', True)
        Category('test_income', False)

    def tearDown(self):
        log = [{}, {}, {}]

    def test_acc(self):
        """testing account object"""

        ac = log[0]['test_ac']
        self.assertTrue(ac)
        self.assertEqual(Decimal('100.00'), ac.value)

    def test_cat(self):
        """testing category object"""

        cat = log[1]['init_new_account']
        self.assertTrue(cat)
        self.assertFalse(cat.value)

    def test_tr_outcome(self):
        """testing  outcome"""

        ac = log[0]['test_ac']
        cat = log[1]['test_cat']
        tr = Transaction(10, ac, cat)
        self.assertEqual(Decimal('10'), tr.value)
        self.assertEqual(Decimal('90'), ac.value)
        self.assertTrue(tr, log[2][tr.name])

    def test_tr_income(self):
        """testing  income"""

        ac = log[0]['test_ac']
        cat = log[1]['test_income']
        tr = Transaction(10, ac, cat)
        self.assertEqual(Decimal('10'), tr.value)
        self.assertEqual(Decimal('110'), ac.value)
        self.assertTrue(tr, log[2][tr.name])

    def test_balance(self):
        """testing balance"""

        ac = log[0]['test_ac']
        time.sleep(1)
        Transaction(20, ac, log[1]['test_cat'])
        time.sleep(1)
        Transaction(10, ac, log[1]['test_income'])
        balance_count()
        self.assertEqual(balance_count(), Decimal('90'))


if __name__ == '__main__':

    unittest.main()
