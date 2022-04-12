
# abstract class
from abc import ABC, abstractmethod

class Account(ABC):           # abstract class
    def __init__(self):
        print("Accounts.....")

    @abstractmethod
    def getBalance(self):
        pass

    def test(self):
        print("hello")

class Savings(Account):
    def deposit(self):
        print("Amount credited........")

    def getBalance(self):
        print("Balance in the account is #####.##")

    def test(self):
        print("world")


sa = Savings()
sa.deposit()
sa.getBalance()
sa.test()
