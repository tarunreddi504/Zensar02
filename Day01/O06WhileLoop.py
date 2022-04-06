
i = 0
while(i < 10):
    print(i, end=" ")
    i += 1
print()

print("-" * 40)
print(f"i :{i}")

while(True):
    print(i, end=" ")
    i -= 1
    if i < 0:
        break
print()

print(f"i :{i}")
