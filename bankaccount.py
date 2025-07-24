with open("C:\\Python-Workspace\\Python\\Bank Management System\\data.txt") as f:
    balance = f.read()

class BankAccount:
    def __init__(self, account_number, name):
        self.acc_number = account_number
        self.name = name
        self.balance = int(balance)

    def withdraw(self, amount):
        if amount > self.balance:
            print("Insufficient Funds")
        else:
            self.balance -= amount
            with open("C:\\Python-Workspace\\Python\\Bank Management System\\data.txt", mode="w") as f:
                f.write(str(self.balance))
            print(f"Withdraw: {amount} Balance: {self.balance}")

    def deposit(self, amount):
        if amount > 0:
            self.balance += amount
            with open("C:\\Python-Workspace\\Python\\Bank Management System\\data.txt", mode="w") as f:
                f.write(str(self.balance))
            print(f"Deposited: {amount} Balance: {self.balance}")
        else:
            print("Invalid Deposit Account")

    def display_balance(self):
        print(f"Account Number: {self.acc_number} Name: {self.name} Balance: {self.balance}")

    def dashboard(self):
        print("1. Withdraw")
        print("2. Deposit")
        print("3. Show Balance")    