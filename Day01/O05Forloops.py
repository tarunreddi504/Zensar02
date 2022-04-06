
# for loop
"""
print(data, sep=, end="\n")

a. continue
b. break
c. else
"""

for i in range(1,11):
    print(i, end=" ")
print()

print("-" * 40)

for i in range(1, 21):
    if i % 2 != 0:
        continue
    if i > 14:
        break
    print(i, end=" ")
print()

print("-" * 40)
for i in range(1, 11):
    print(i, end=" ")
else:
    print("\nIteration in completed...")

