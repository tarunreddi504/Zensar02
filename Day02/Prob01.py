
l1 = [1, 2, 3, 1, 2, 1, 2, 1, 3, 1, 1, 2, 1, 1, 1, 1, 4, 1, 2, 1, 1 ,1 ,1]

while(True):
    try:
        l1.remove(1)
    except ValueError:
        break

print(l1)


print("-" * 40)

p=[1, 2, 3, 4, [10, 20, 30, 40, 50], 6, 7, [11, 12, 13, 14, 15], 9, 10]
p[4].clear()
p[7].clear()
print(p)