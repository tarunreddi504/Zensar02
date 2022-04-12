
from abc import ABC, abstractmethod

class Employee(ABC):

    @abstractmethod
    def doJob(self):
        pass

class Manager(Employee):

    def doJob(self):
        print("Managers job.....")

class Developer(Employee):

    def doJob(self):
        print("Coding job.......")

def BankFun(emp):           # polymorphism
    print("BankjobStarted......".center(40, "-"))
    emp.doJob()
    print("BankjobCompleted.....".center(40, "-"))
    print("-" * 40)

Alan = Manager()
Mark = Developer()


BankFun(Alan)
BankFun(Mark)

print("-" * 40)
def BankFunJobs(emps):           # polymorphism
    print("BankjobStarted......".center(40, "-"))
    for emp in emps:
        emp.doJob()
    print("BankjobCompleted.....".center(40, "-"))
    print("-" * 40)

BankFunJobs([Alan, Mark])
