
class Employee:

    def __init__(self, name, salary):
        self.name = name
        self.salary = salary
        self.tech = ['java', 'j2ee', 'spring', 'hibernate', 'angular', 'react']

    def __str__(self):
        return f"Name = {self.name}\nSalary = {self.salary}"

    def __add__(self, other):
        return Employee("Noname", self.salary + other.salary)

    def __len__(self):
        return len(self.tech)

    def __iter__(self):
        return iter(self.tech)


emp1 = Employee("Micheal", 35000)
print(emp1)

print("-" * 40)
emp2 = Employee("Louis", 45000)
print(emp2)

print("-" * 40)
print(emp1 + emp2)

print("-" * 40)
print(len(emp1))

print("-" * 40)
print([t for t in emp1])
