class BankAccount:
    all_accounts = []

    def __init__(self,balance=0):
        self.balance = balance
        self.account_number
        self.self_account_list = []

    def create_account(self):
        for self.account_number in range(0,100):
            self.account_number = self.account_number + 1
            BankAccount.all_accounts.append(self)
            self.self_account_list.append(self)
            print(self.account_number)
            return self

class User:
    def __init__(self,name):
        self.user_bank_account = BankAccount
        self.name = name

user_1 = User("Jack")

user_1.user_bank_account.create_account()