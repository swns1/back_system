from bankaccount import BankAccount

class SavingsAcount(BankAccount):
    def __init__(self, account_number, name):
        super().__init__(account_number, name)
        self.interest_rate = 0.02
        self.interest = 0

    def apply_interest(self):
        self.interest = self.balance * self.interest_rate
        self.balance += self.interest
    
    def display_balance(self):
        print(f"Account Number: {self.acc_number} Name: {self.name} Balance: {self.balance} Interest Acquired: {self.interest}")