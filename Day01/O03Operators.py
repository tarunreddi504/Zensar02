"""
a. arithmetic
b. relational
c. assignment
d. logical
e. bitwise
f. membership
g. identity

"""

print("Arithematic Operators".center(40, "-"))
print(10 + 3)
print(10 - 3)
print(10 * 3)
print(10 / 3)
print(10 // 3)      # floor division
print("-" * 40)
print(10 % 3)
print("-" * 40)
print(10 ** 3)

print("Augmentor".center(40, "-"))
# =, +=, -=, *=, /=
x = 10
print(f"x :{x}")
x += 5      # x = x + 5
print(f"x :{x}")

print("-" * 40)
x //= 3
print(f"x :{x}")

print("Relational Operators".center(40, "-"))
# ==, >=,  <=, !=
a = 10
b = 12
print(f"a, b : {a, b}")
print(f"a == b :{a == b}")
print(f"a >= b :{a >= b}")
print(f"a <= b :{a <= b}")
print(f"a != b :{a != b}")

print("Logical Operators".center(40,"-"))
a = 10
b = 15
print(b > a and a < b)
print(a < b and a > b)

print("-" * 40)
print(b > a or a < b)
print(a < b or a > b)

print("-" * 40)
print(f'a :{ord("a")}')
print(f'A :{ord("A")}')
print(f'o :{ord("o")}')
print(f'O :{ord("O")}')

print("-" * 40)
print("apple" > "orange")
print("orange" > "apple")

print("Bitwise Operators".center(40, "-"))
print(5 | 3)
"""
5  - 0101
3  - 0011
    ------
7  - 0111
    ------
    
0101 => 10100
1000 => 10000
0101 >> 1 => 0010
"""
print(5 & 3)
print(5 ^ 3)
print(5 << 1)
print(8 << 1)
print(5 << 2)
print(5 >> 1)
print(~0)                   # complement operator
print(~1)                   # 0000 => 1111, 0001 => 1110

print("Ternary operator".center(40, "-"))
a = 18
print("eligible" if a >= 18 else "not eligible")

print("Identity Operator".center(40, "-"))

print(2 is 2)
print(1 is 10)
print("1" is "1")
print(2 is not "2")

