
class Employee:

    def __init__(self, name):
        self.__name = name          # private variable
        self.tech = ['java', 'spring', 'j2ee', 'hibernate', 'ejb', 'angular']

    def __str__(self):
        return self.__name + " and tech :" + ", ".join([v for v in self.tech])

emp1 = Employee("Mark")
print(emp1)

print("-" * 40)
# print(emp1.__name)
print(emp1.__dict__)
emp1._Employee__name = "Steve"
print(emp1)