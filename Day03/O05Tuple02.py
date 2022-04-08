
from collections import namedtuple

nmdTpl = namedtuple("Students", "studid sname age clas gender")
stud = nmdTpl(studid=10, sname="Glen", age= 15, clas=9, gender="m")
print(f"emp :{stud}")
print(f"Student ID     :{stud.studid}")
print(f"Student name   :{stud.sname}")
print(f"Student Age    :{stud.age}")
print(f"Student Class  :{stud.clas}")
print(f"Student Gender :{stud.gender}")

print("-" * 40)
print(stud)
# stud.age = 18
print("-" * 40)
stud1 = nmdTpl(studid=25, sname="Tina", age= 14, clas=8, gender="f")
print(f"emp :{stud1}")
print(f"Student ID     :{stud1.studid}")
print(f"Student name   :{stud1.sname}")
print(f"Student Age    :{stud1.age}")
print(f"Student Class  :{stud1.clas}")
print(f"Student Gender :{stud1.gender}")

print("-" * 40)

def arithmaticCalc(x, y):
    sum = x + y
    diff = x - y
    prod = x * y
    quot = x / y
    tpl = namedtuple("arithmatic", "sum diff prod quot")
    res = tpl(sum = sum, diff = diff, prod = prod, quot = quot)
    return res

r = arithmaticCalc(20, 8)
print(f'r :{r}')
print(r.sum)
print(r.diff)
print(r.prod)
print(r.quot)

