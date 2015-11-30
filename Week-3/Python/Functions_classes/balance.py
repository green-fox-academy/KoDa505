class BankAccount:
    def __init__(self, name, origbalance = 0):
        self.balance = origbalance
        self.name = name

    def deposit(self, amount):
        self.balance += amount
        return self.balance

    def withdraw(self, amount):
        self.balance  -= amount
        return self.balance
