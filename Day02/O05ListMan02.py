"""
'append', 'clear', 'copy', 'count', 'extend', 'index',
'insert', 'pop', 'remove', 'reverse', 'sort'
"""
# funtions to add elements into a list
# 1.append, 2.extend, 3.insert

print("append".center(40, "-"))
l1 = list(range(1, 6))
print(f"l1 :{l1}")

l1.append(6)
l1.append(7)
l1.append(8)
print(f"l1 :{l1}")
l1.append([9, 10, 11, 12, 13])
print(f"l1 :{l1}")                  # converts into a two dimensional array
print(l1[8][1:4])
print(f"{l1[-1][-2:-5:-1]}")

print("{:-^40}".format("extend"))
l2 = [11, 12, 13, 14, 15]
print(f"l2 :{l2}")
l2.extend([16, 17, 18])
print(f"l2 :{l2}")
l2.extend([19, 20, 21])
print(f"l2 :{l2}")

print("insert".center(40, "-"))
l3 = [2, 4, 6, 8, 10]
print(f"l3: {l3}")

l3.insert(0, 1)
l3.insert(2, 3)
l3.insert(4, 5)
print(f"l3: {l3}")

# Remove elements from a list
# 1.pop, 2.remove, 3.clear
print("{:-^40}".format("pop"))
l1 = list(range(1, 11))
print(f"l1 :{l1}")

res = l1.pop(0)
print(f"res :{res}")

res1 = l1.pop(3)
print(f"res1 :{res1}")

res2 = l1.pop()
print(f"res2 :{res2}")

l1.pop()
print(f"l1 :{l1}")

print("remove".center(40, "-"))
l2 = [1, 2, 3, 1, 2, 1, 2, 1, 3, 1, 1, 2, 1, 4, 1, 2, 1]
print(f"l2 :{l2}")
res = l2.remove(1)
print(f"res :{res}")
l2.remove(3)
print(f"l2 :{l2}")

print("clear".center(40, "-"))
l3 = list(range(1, 6))
print(f"l3 :{l3}")
l3.clear()
print(f"l3 :{l3}")
