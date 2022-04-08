
print("items".center(40, "-"))
emp = {
    'emp1': {'empid': 1023, 'empname': 'Smith', 'age': 32, 'desig': 'Tl', 'dept': 'MKT', 'sal': 86500},
    'emp2': {'empid': 2689, 'empname': 'Jane', 'age': 36, 'desig': 'MGR', 'dept': 'Finance', 'sal': 165000},
    'emp3': {'empid': 3012, 'empname': 'Loius', 'age': 34, 'desig': 'BDM', 'dept': 'MKT', 'sal': 115000}
}

print(f"emp :{emp}")

print("-" * 40)
print(f"emp1 :{emp['emp1']}")

print("-" * 40)
print(f"emp2 :{emp['emp2']}")

print("-" * 40)
print(f"emp3 :{emp['emp3']}")

print("-" * 40)
# items = keys + values
for ky, info in emp.items():
    print(ky)
    print("-----")
    for k, v in info.items():
        print(k, "=>", v)
    print("-" * 40)

print("-" * 40)
emp1 = {'empid': 1023, 'empname': 'Smith', 'age': 32, 'desig': 'Tl', 'dept': 'MKT', 'sal': 86500}

print(f"emp1 :{emp1}")
# keys() - get all the keys from the dictionary
# values() - get all the values from the dictionary

k = emp1.keys()
print(f"k :{k}")

v = emp1.values()
print(f"v :{v}")

print("-" * 40)
# items  - get both keys and values from the dictionary
for k, v  in emp1.items():
    print(k, "-", v)

print("update".center(40, "-"))
# update values from emp2 to emp1 => emp1 is the target and emp2 is the source
emp1 = {'empid': 1023, 'empname': 'Smith', 'age': 32, 'desig': 'Tl', 'dept': 'MKT'}
emp2 = {'empid': 2689, 'empname': 'Jane', 'age': 36, 'desig': 'MGR', 'sal': 165000}

print(f"emp1 :{emp1}")
print(f"emp2 :{emp2}")

emp1.update(emp2)
print(f"emp1 :{emp1}")

print("clear".center(40, "-"))
emp1 = {'empid': 1023, 'empname': 'Smith', 'age': 32, 'desig': 'Tl', 'dept': 'MKT'}
print(f"emp1 :{emp1}")

emp1.clear()
print(f"emp1 :{emp1}")
