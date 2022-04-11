
def addMe(x, y):
    return x + y

a = addMe

print(f"The sum of 10 and 20 is :{a(10, 20)}")

print("-" * 40)

b = lambda x, y: x + y
res = b(30, 40)
print(f"res :{res}")

# lambdas are best used with functions like MAP, FILTER and REDUCE(functool)

# MAP
l = list(range(1, 11))
print(f"l :{l}")

res = list(map(lambda x: x ** 2, l))
print(f'res :{res}')

months = ['dec', 'aug', 'oct', 'nov', 'sep', 'jan', 'apr', 'mar', 'jul', 'feb', 'jun', 'may']
print(f"months :{months}")
from calendar import month_name

srtdMons = sorted(months, key=list(map(lambda m: m[0:3].lower(), list(month_name))).index)
print(f"sorted months :{srtdMons}")

print("filter".center(40, "-"))
l = list(range(1, 21))
print(f"l :{l}")

res = list(filter(lambda x: x % 3 == 0, l))
print(f"res :{res}")

print("Reduce".center(40, '-'))
l = [4, 9, 6, 2, 5, 8, 10, 15, 9, 12, 11]

from functools import reduce
res = reduce(lambda x, y: x if x > y else y, l)
print(f"res :{res}")

"""
temp = (23, 30, 25, 32, 38, 40, 43, 49, 20, 18) - temp to be converted from celsius to farenheit
expenses = (12, 30, 25, 50, 85, 100, 500, 250, 1600) => covert dollars to rupees

"""