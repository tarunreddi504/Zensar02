
class Employee:

    def __init__(self, name, salary):
        self.name = name
        self.salary = salary

    def __str__(self):
        return f"Name = {self.name}\nSalary = {self.salary}"

    def __add__(self, other):
        return self.salary + other.salary

    def __sub__(self, other):
        return self.salary - other.salary

    def __mul__(self, other):
        return self.salary * other.salary

    def __truediv__(self, other):
        return self.salary / other.salary

    def __floordiv__(self, other):
        return self.salary // other.salary


emp1 = Employee("Mike", 65000)
print(emp1)

print('-' * 40)
emp2 = Employee("Janet", 15000)
print(emp2)

print('-' * 40)
print("Sum :", emp1 + emp2)

print('-' * 40)
print("Subtract :", emp1 - emp2)

print('-' * 40)
print("Multiplication :", emp1 * emp2)

print('-' * 40)
print("Division :", emp1 / emp2)

print('-' * 40)
print("Floor Division :", emp1 // emp2)
