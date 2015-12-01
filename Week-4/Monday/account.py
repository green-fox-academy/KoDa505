class BankAccount:
    def __init__(self, name, balance):
        self.name = name
        self.balance = balance

    def pay(self, amount):
        self.balance -= amount
    #    return self.balance  itt most nem kell, mert ennek most tk csak mellekhatasa lesz

    def receive(self, amount):
        self.balance += amount
    #    return self.balance  - nem pontosan ertem, hogy miert, de nem kell ide a return

    def print_balance(self):
        print("Balance of")
        print(self.name)
        print('is: ')
        print(self.balance)

    '''
    def transfer(self, other, amount):   # ez az eredeti megoldas
        self.balance -= amount
        other.balance += amount
    '''

    def transfer(self, other, amount):
        self.pay(amount)
        other.receive(amount)

bela = BankAccount('Bela', 300)
feri = BankAccount('Feri', 400)

bela.receive(130000)
bela.transfer(feri, 59)

bela.print_balance()
feri.print_balance()
