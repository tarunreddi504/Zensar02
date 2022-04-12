
class Employee:

    def __init__(self, name):
        self.name = name
        self.tech = ['java', 'j2ee', 'spring', 'hibernate', 'angular', 'react'];

    def __iter__(self):
        return iter(self.tech)

    def append(self, val):
        self.tech.append(val)

    def __getitem__(self, index):
        return self.tech[index]

    def __setitem__(self, index, value):
        self.tech[index] = value

emp1 = Employee("")

print([e for e in emp1])

print("-" * 40)
emp1.append("python")
print([e for e in emp1])

print("-" * 40)
x = emp1[3]
print(f"x :{x}")

print("-" * 40)
emp1[2] = "JSP"

print([e for e in emp1])
