
"""
'clear', 'copy', 'fromkeys', 'get', 'items', 'keys',
'pop', 'popitem', 'setdefault', 'update', 'values'
"""

print("{:-^40}".format("get"))
fruits = {'apple': 280, 'orange': 80, 'watermelon': 120, 'gauva': 40, 'banana': 60}
print(f"fruits :{fruits}")

price = fruits.get('orange')
print(f"price :{price}")

price = fruits.get('grapes')
print(f"price :{price}")

price = fruits.get('grapes', "Invalid key, please enter a valid key.....")
print(f"price :{price}")

print('keys'.center(40, "-"))
fruits = {'apple': 280, 'orange': 80, 'watermelon': 120, 'gauva': 40, 'banana': 60}
print(f"fruits :{fruits}")

k = fruits.keys()
print(f"k :{k}")
for i in k:
    print(i, end=" ")
print()

print("-" * 40)
for k  in fruits.keys():
    print(k + " => " + str(fruits[k]))

print("-" * 40)
for x in fruits:            # this will always point to the dictionary keys
    print(f"{x} => {fruits[x]}")

print("values".center(40, "-"))
emp = {'name': 'Micheal', 'age': 38, 'desig': 'TL', 'dept': "MKT", 'sal': 85000}
print(f"emp :{emp}")
print(emp.values())

print("set default".center(40, "-"))
# set default is used to add new key values into the dictionary
emp = {'name': 'Micheal', 'age': 38, 'desig': 'TL', 'dept': "MKT", 'sal': 85000}

emp.setdefault('loc', 'Bangalore')              # added into the dictionary
emp.setdefault('age', 40)                       # will not get added, as the key is already existing
print(f"emp :{emp}")

print("{:-^40}".format("fromkeys"))
# to convert a list into a dictionary, element of the list will become the keys
cities = ['blr', 'che', 'mum', 'hyd', 'del', 'kol', 'pun']
print(f"cities :{cities}")
print(type(cities))

res1 = dict.fromkeys(cities)
print(f"res1 :{res1}")

res2 = dict.fromkeys(cities, 24)
print(f"res2 :{res2}")

print("pop".center(40, "-"))
veg = {'crt': 25, 'bns': 65, 'rdsh': 50, 'tmt': 15, 'onin': 25, 'chl': 90}
print(f"veg :{veg}")

res = veg.pop('rdsh')           # returns only the value
print(f"res :{res}")

res1 = veg.pop('chl')
print(f"res1 :{res1}")

# res2 = veg.pop('ptat')
# res2 = veg.pop()

print(f"veg :{veg}")

print("popitem".center(40, "-"))
veg = {'crt': 25, 'bns': 65, 'rdsh': 50, 'tmt': 15, 'onin': 25, 'chl': 90}
print(f"veg :{veg}")

res1 = veg.popitem()                # returns both key and value
print(f"res1 :{res1}")

res2 = veg.popitem()
print(f"res2 :{res2}")

print(f"veg :{veg}")
