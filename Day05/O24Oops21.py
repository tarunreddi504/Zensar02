# duck types

class Manager():

    def doJob(self):
        print("Managers job.....")

class Developer():

    def doJob(self):
        print("Coding job.......")

Alan = Manager()
Mark = Developer()

print("-" * 40)
def BankFunJobs(emps):           # polymorphism
    print("BankjobStarted......".center(40, "-"))
    for emp in emps:
        emp.doJob()
    print("BankjobCompleted.....".center(40, "-"))
    print("-" * 40)

BankFunJobs([Alan, Mark])