"""
Numbers
a. integer
b. float
c. complex numbers

conversion function
-------------------
int - float
float - int
int - complex
"""

a = 10
b = -10

print(f"a :{a}")
print(f"type(a) :{type(a)}")
print(f"b :{b}")
print(f"type(a) :{type(a)}")
print("-" * 40)

c = 5.0
d = -5.0
print(f"c :{c}")
print(f"type(c) :{type(c)}")
print(f"d :{d}")
print(f"type(d) :{type(d)}")
print("-" * 40)

e = +2e3
f = -2e3
print(f"e :{e}")
print(type(e))
print(f"f :{f}")
print(type(f))
print("-" * 40)

g = 3 + 4j
h = 3 - 4j
print(f"g :{g}")
print(f"type(g) :{type(g)}")
print(f"h :{h}")
print(f"type(h) :{type(h)}")
print("-" * 40)

x = 3 + 2.5
print(f"x :{x}")
print(f"type(x) :{type(x)}")

x = 2
y = 1.5
z = x + y
print(f"x :{x}")
print(f"y :{y}")
print(f"z :{z}")
print(f"x= {type(x)}")
print(f"y= {type(y)}")
print(f"z= {type(z)}")

print("conversions".center(40, "-"))
a = 10
print(f"{type(a)}\t\t{a}")
print(f"{type(float(a))}\t\t{float(a)}")
print(f"{type(complex(a))}\t\t{complex(a)}")
print(f"{type(bool(a))}\t\t{bool(a)}")

print("Number System".center(40, "-"))
print(11)           # decimal
print(0b11)         # binary
print(0b101)        # binary
print(0o11)         # octal
print(0o111)        # octal
print(0xe)          # hexa
print(0xa)          # hexa

print("Number Conversion System".center(40, "-"))
a = 100
print(f"oct(a) :{oct(a)}")
print(f"hex(a) :{hex(a)}")
print(f"bin(a) :{bin(a)}")

print("Example".rjust(40, "-"))
print("Example".ljust(40, "-"))
print("Example".center(40, "-"))
