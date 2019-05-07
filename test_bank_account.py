import unittest
from bank_account import BankAccount, MiniumBalanceAccount


class AccountBalanceTestCase(unittest.TestCase):
    def setUp(self):
        self.account_lekan = BankAccount()

    def test_balance(self):
        self.assertEqual(self.account_lekan, 3000,
                         msg='Account Balance Invalid.')

    def test_deposit(self):
        self.account_lekan.deposit(4000)
        self.assertEqual(self.account_lekan.balance, 7000,
                         msg='Deposit method Inaccurate.')

    def test_withdraw(self):
        self.account_lekan.withdraw(500)
        self.assertEqual(self.account_lekan.balance, 2500,
                         msg='Withdraw method Inaccurate.')

    def test_invalid_transaction(self):
        self.assertEqual(self.account_lekan.withdraw(
            6000), "Invalid Transaction", msg='Invalid Transaction.')

    def test_sub_class(self):
        self.assertTrue(issubclass(MiniumBalanceAccount, BankAccount),
                        msg='Not true subclass of bank Account')
