class BankAccount:
    def __init__(self, balance):
        self.__balance = balance

    def deposit(self, amount):
        self.__balance += amount

    def withdraw(self, amount):
        if amount <= self.__balance:
            self.__balance -= amount
        else:
            print("Insufficient Balance")

    def show_balance(self):
        print("Balance =", self.__balance)

acc = BankAccount(5000)

acc.deposit(1000)
acc.withdraw(2000)

acc.show_balance()
