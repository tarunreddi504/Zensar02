
# convert the string into a list
print("split".center(40, "-"))
emp = "emp004, Mike Tyson, 55, MGR, Boxing, 250000"
print(f"emp :{emp}")
res = emp.split(", ")
print(f"res :{res}")
print(type(res))
sport = emp.split(", ")[4]
print(F"sport :{sport}")

print("-" * 40)
print(f"res :{res}")
emp1 = ", ".join(res)
print(f"emp1 :{emp1}")
print(type(emp1))

