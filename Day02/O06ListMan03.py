
print("{:-^40}".format("count"))

l1 = [1, 2, 3, 1, 2, 1, 2, 1, 3, 1, 1, 2, 1, 1, 1, 1, 4, 1, 2, 1, 1 ,1 ,1]
print(f"1 :{l1.count(1)}")
print(f"2 :{l1.count(2)}")
print(f"3 :{l1.count(3)}")

print("index".center(40,"-"))
l2 = [1, 2, 3, 1, 2, 3, 4, 1, 2, 1, 2 , 1, 3, 1, 4]
print(l2.index(1))
print(l2.index(4))
print(l2.index(4, 7))

# copy function
print("copy".center(40, "-"))
l1 = [1, 2, 3, 4, 5]
print(f"l1 Before :{l1}")
l2 = l1                 # shallow copy => its not only sharing the data but also sharing its address
print(f"l2 Before :{l2}")

l2.extend([6, 7, 8, 9])
print(f"l2 After :{l2}")
print(f"l1 After :{l1}")

print("-" * 40)
l3 = [6, 7, 8, 9, 10]
print(f"l3 Before :{l3}")
l4 = l3.copy()              # deep copy - where the only the data is shared
print(f"l4 Before :{l4}")

l4.insert(0, 5)
l4.insert(0, 4)
l4.insert(0, 3)
print(f"l4 After :{l4}")
print(f"l3 After :{l3}")

print("-" * 40)
l5 = [10, 20, 30, 40, [5, 15, 25, 35, 45], 50]
print(f"l5 Before :{l5}")
l6 = l5.copy()                  # deep copy (only for outer layer)
print(f"l6  Before :{l6}")

l6[4].insert(1, 10)
l6[4].insert(3, 20)
l6[4].insert(5, 30)
print(f"l6 After :{l6}")
print(f"l5 After :{l5}")

print("-" * 40)
from copy import deepcopy
l7 = [2, 4, 6, 8, [1, 3, 5, 7, 9], 10]
print(f"l7 Before :{l7}")
l8 = deepcopy(l7)
print(f"l8 Before :{l8}")

l8[4].insert(1, 2)
l8[4].insert(3, 4)
l8[4].insert(5, 6)
print(f"l8 After :{l8}")
print(f"l7 After :{l7}")

print("{:-^40}".format('sort'))
"""
sort vs sorted
--------------
sort -> alrter the original list
sorted -> return a copy of the sorted list

"""
l = [9, 5, 8, 1, 10, 4, 2, 6, 3, 7]
print(f"l :{l}")
res1 = sorted(l)
print(f"res1 :{res1}")
res2 = sorted(l, reverse=True)
print(f"res2 :{res2}")

print("-" * 40)
l = [9, 'zebra', 'apple',5, 'yellow', 'blue', 8, 'green', 'violet', 1, 'pink', 'orange', 10,
     4, 'red', 'dog', 2, 'cat', 'snake', 6, 1024, 19, 120, 1452, 3, 28, 215, 2098, 7]
print(f"l :{l}")

print("-" * 40)
res = sorted(l, key=ascii)
print(f"res :{res}")

print("-" * 40)
cities = ['thiruvananthapuram', 'hyderabad', 'chennai', 'ooty', 'bangalore', 'mumbai', 'pune',
          'vishakapatnam', 'coimbatore', 'kanyakumari', 'delhi', 'mysore']
print(f"cities :{cities}")

print("-" * 40)
res = sorted(cities, key=len, reverse=True)
print(f"res :{res}")

print("reversed".center(40, "-"))
l = [9, 5, 8, 1, 10, 4, 2, 6, 3, 7]
print(f"l :{l}")
res = list(reversed(l))
print(f"res :{res}")
