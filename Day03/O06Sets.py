
s1 = set()
print(f's1 :{s1}')
print(type(s1))

print("-" * 40)
s2 = {1, 2, 3 ,4 , 4, 5, 1, 2, 3}
print(f"s2 :{s2}")
print(type(s2))

print("-" * 40)
s3 = set(range(1, 10))
print(f"s3 :{s3}")
print(type(s3))

print("-" * 40)
l1 = list(s3)
print(f"l1 :{l1}")
print(type(l1))

print("-" * 40)
s3 = set(range(1, 10))
print(f"s3 :{s3}")

for i in s3:
    print(i, end=' ')
print()

print("-" * 40)
s4 = {1, 2}
print(f"s4 :{s4}")
s4.add(1)
s4.add(3)
s4.add(1)
s4.add(2)
print(f"s4 :{s4}")

print("update".center(40, "-"))
print(f"s4 :{s4}")
s4.update([1, 2])
s4.update([2, 3, 4])
s4.update([3, 4, 5])
s4.update([6, 7, 8])
print(f"s4 :{s4}")

print("pop".center(40, "-"))
print(f"s4 :{s4}")
res = s4.pop()
print(f"res :{res}")
print(f"s4 :{s4}")

res = s4.pop()
print(f"res :{res}")
print(f"s4 :{s4}")

print("remove".center(40,"-"))
print(f"s4 :{s4}")
s4.remove(5)
s4.remove(7)

print(f"s4 :{s4}")

print("discard".center(40, "-"))
print(f"s4 :{s4}")
s4.discard(6)
s4.discard(10)
print(f"s4 :{s4}")

print("-" * 40)
A = {1, 2, 3, 4, 5, 6}
B = {5, 6, 7, 8, 9, 10}

print(f"A :{A}")
print(f"B :{B}")

print("-" * 40)
print("A union B :", A | B)
print("B union A :", B.union(A))

print("-" * 40)
print("A intersection B :", A & B)
print("B intersection A :", B.intersection(A))

print("-" * 40)
print("A difference B :", A - B)
print("B difference A :", B - A)

print("-" * 40)
print("A symmetric difference B :", A ^ B)
print("B symmetric difference A :", B.symmetric_difference(A))

print("-" * 40)
# frozen_set - immutable
fs = frozenset([1, 2, 3 ,4, 5])
print(f"fs :{fs}")
