import banking

class TestBankAccount:

    def test_deposit(self):
        ob = banking.BankAccount(123123, 1000)
        ob.deposit(80)
        ob.deposit(120)
        ob.deposit(400)
        assert ob.balance == 1600

    def test_withdraw(self):
        ob = banking.BankAccount(123123, 1000)
        ob.withdraw(80)
        ob.withdraw(120)
        ob.withdraw(400)
        assert ob.balance == 400
