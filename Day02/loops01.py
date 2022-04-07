
for i in range(1, 11):
    print(i)

print("-" * 40)

for i in range(1, 6):
    # print(i)
    for j in range(1, 4):               # 3 =>  4 x 3 = 12
        print(j, end=" ")
    print()

print("-" * 40)

for i in range(1, 6):
    for k in range(5, i, -1):           # 5, 4, 3, 2; 5, 4, 3; 5, 4; 5
        print(" ", end="")
    for j in range(1, i+1):
        print(j, end=" ")
    print()