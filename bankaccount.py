class BankAccount:
    def __init__(self, account_number, name, balance):
        self.acc_number = account_number
        self.name = name
        self.balance = balance

    def withdraw(self, amount):
        if amount > self.balance:
            print("Insufficient Funds")
        else:
            self.balance -= amount
            print(f"Withdraw: {amount} Balance: {self.balance}")

    def deposit(self, amount):
        if amount > 0:
            self.balance += amount
            print(f"Deposited: {amount} Balance: {self.balance}")
        else:
            print("Invalid Deposit Account")

    def display_balance(self):
        print(f"Account Number: {self.acc_number} Name: {self.name} Balance: {self.balance}")

    def dashboard(self):
        print("1. Withdraw")
        print("2. Deposit")
        print("3. Show Balance")    