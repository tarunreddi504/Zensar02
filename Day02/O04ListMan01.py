
# lists
l1 = list()
print(f"l1 :{l1}")
print(type(l1))

print("-" * 40)
l2 = [1, 2, 3.5, 4.9, 'five', 'six', True, False, 3+ 4j]
print(f"l2 :{l2}")
print(type(l2))

print("-" * 40)
l3 = list(range(1, 11))
print(f"l3 :{l3}")
print(type(l3))

print("-" * 40)
l4 = [1, 2, 3, 4.5, 5.2, 6.8, 'seven', 'eight', 'nine', True, False, 12+0j, 13-1j]
print(f"l4 :{l4}")
print(type(l4))

print(f"l4[0] :{l4[0]}")
print(f"l4[6] :{l4[6]}")

# memory allocation is not contigious
print("-" * 40)
print(f"l4[0] :{id(l4[0])}")
print(f"l4[1] :{id(l4[1])}")
print(f"l4[2] :{id(l4[2])}")
print(f"l4[3] :{id(l4[3])}")
print(f"l4[4] :{id(l4[4])}")
print(f"l4[5] :{id(l4[5])}")
print(f"l4[6] :{id(l4[6])}")

print("-" * 40)
l1 = list(range(1, 11))
print(f"l1 :{l1}")

print(f"l1[0] :{l1[0]}")
print(f"l1[9] :{l1[9]}")

print(f"l1[-1] :{l1[-1]}")
print(f"l1[-3] :{l1[-3]}")

# slicing
print(f"l1 :{l1}")
print(f"l1[3:8] :{l1[3:8]}")
print(f"l1[0:7] :{l1[0:7]}")
print(f"l1[0:]  :{l1[0:]}")
print(f"l1[:10] :{l1[:10]}")
print(f"l1[:]   :{l1[:]}")

# reverse indexing
print("-" * 40)
l2 = list(range(3, 25, 3))
print(f"l2 :{l2}")
print(f"l2[-1] :{l2[-1]}")
print(f"l2[-6] :{l2[-6]}")
print(f"l2[-8] :{l2[-8]}")

# slicing with reverse indexing
l2 = list(range(2, 20, 2))
print(f"l2 :{l2}")
print(f"l2[-1:-6:-1] :{l2[-1:-6:-1]}")
print(f"l2[-5:-10:-1] :{l2[-5:-10:-1]}")
print(f"l2[-1::-1]    :{l2[-1::-1]}")
print(f"l2[:-10:-1]   :{l2[:-10:-1]}")
print(f"l2[::-1]      :{l2[::-1]}")

print("-" * 40)
l = list(range(1, 6))
print(f"l :{l}")
l[2] = "three"              # expecting the number to get added
print(f"l :{l}")
# l[5] = 6
# print(f"l :{l}")

print("-" * 40)
print(dir(l))
