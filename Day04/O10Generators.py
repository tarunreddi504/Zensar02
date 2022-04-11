
from sys import getsizeof

val1 = [x ** 2 for x in range(1, 1000)]                   # compreshension
# print(f"val1 :{val1}")

val2 = (x ** 2 for x in range(1, 1000))                   # generator
# print(f"val2 :{val2}")

print("-" * 40)

val1 = [x ** 2 for x in range(1, 10000)]

val2 = (x ** 2 for x in range(1, 10000))


print("Comprehension size of lst    :", getsizeof(val1))
print("Generator size of lst        :", getsizeof(val2))
