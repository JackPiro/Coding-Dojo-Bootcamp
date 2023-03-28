class BankAccount:
    
    all_accounts = []
    balance = 0

    def __init__(self,balance,account_number):
        self.balance = balance
        BankAccount.all_accounts.append(self)
        self.bank_interest = 0.03
        self.account_number = account_number
    
    def deposit(self,amount):
        self.balance = self.balance + amount
        print(self.balance)
        return self

    def withdrawl(self, amount):
        if self.balance < amount:
            print("Insufficient funds")
            return self
        else:
            self.balance = self.balance - amount
            return self
    def display_account_info(self):
        print(self.balance)
        return self

    def yield_interest(self,time_in_months):
        self.balance = self.bank_interest * time_in_months + self.balance
        print(self.balance)
        return self

class User:
    def __init__(self,name):
        self.name = name
        self.account = BankAccount
        # self.account_number = account_number

    def make_deposit(self,amount):
        self.account.deposit(self.account, amount)
        return self

    def make_withdrawl(self,amount):
        self.account.withdrawl(self.account, amount)
        return self

    def display_user_balance(self):
        self.account.display_account_info(self.account)
        return self

    # def create_bank_account(self,account_number):



user_1 = User("Jack")
user_2 = User("Emily")

user_1.make_deposit(100).display_user_balance()
user_2.make_deposit(1500)