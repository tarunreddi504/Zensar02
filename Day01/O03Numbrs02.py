
import random

print(random.random())
print(random.random())
print(random.random())
print(random.random())
print("-" * 40)

print(random.randint(1, 10))
print(random.randint(1, 25))
print(random.randint(1, 50))
print(random.randint(1, 100))
print("-" * 40)

lst = [10, 20, 30, 40, 50, 60]
print(f"lst :{lst}")
print(random.choice(lst))
print(random.choice(lst))
print(random.sample(lst, 3))
print(random.sample(lst, 3))

print("-" * 40)
import math
print(f"Ceil 2.1 -", math.ceil(2.1))
print(f"Ceil 2.3 -", math.ceil(2.1))
print(f"Ceil 2.5 -", math.ceil(2.1))
print(f"Ceil 2.7 -", math.ceil(2.1))

print("-" * 40)
print(f"Floor 2.1 -", math.floor(2.1))
print(f"Floor 2.3 -", math.floor(2.3))
print(f"Floor 2.5 -", math.floor(2.5))
print(f"Floor 2.7 -", math.floor(2.7))

print("-" * 40)
print(f"round 2.1 -", round(2.1))
print(f"round 2.3 -", round(2.3))
print(f"round 2.5 -", round(2.5))
print(f"round 2.7 -", round(2.7))
