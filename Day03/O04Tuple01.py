
t1 = tuple()
print(f"t1 :{t1}")
print(type(t1))

print("-" * 40)
t2 = (1, 2, 3, 4, 5)
print(f"t2 :{t2}")
print(type(t2))

print("-" * 40)
t3 = tuple(range(1, 10, 2))
print(f"t3 :{t3}")
print(type(t3))

print("-" * 40)
t4 = 1,
print(f"t4 :{t4}")
print(type(t4))

print("-" * 40)
t5 = 1, 2, 3, 4, 5
print(f"t5 :{t5}")
print(type(t5))

print("-" * 40)
t = (1, 2, 3, 4, 5.1, 6.2, 7.9, 'eight', 'nine', 'ten', True, False)
print(f"t :{t}")

print(t[7])
print(t[0:5])
print(t[-1])
print(t[-1:-6:-1])

# t[7] = 8            # immutable
# print("-" * 40)
# print(dir(t))

print("-" * 40)
t = (1, 2, 3, 1, 2, 1, 2, 1, 1, 3, 4, 2, 1, 2, 3, 1, 2, 5)
print(f"t :{t}")
print(type(t))

print(f"1 :{t.count(1)}")
print(f"2 :{t.count(2)}")
print(f"3 :{t.count(3)}")

print("-" * 40)
print(t.index(2))
print(t.index(3))
print(t.index(3, 4))
print(t.index(3, 10))
