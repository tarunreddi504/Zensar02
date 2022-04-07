
# Conversions
print("conversions".center(40, "-"))
print("{val} {val} {val}".format(val="A"))
print("{val!s} {val!r} {val!a}".format(val="A"))

print("{num} {num} {num}".format(num = 36))
print("{num} {num:f} {num:b}".format(num = 36))             # Binary and Float
print("{num:10} {num:f} {num:b}".format(num = 36))
print("{num:5} {num:f} {num:b}".format(num = 36))
print("{num:5} {num:f} {num:b}".format(num = 3656756))

print("Alignment".center(40, "-"))
print("{num:10}Tendulkar".format(num=3))                    # right aligned
print("{num:10}Tendulkar".format(num="Sachin"))             # left aligned
print("{}".format("Sachin Tendulkar"))
print("{:.6}".format("Sachin Tendulkar"))
print("{:.4}".format("Sachin Tendulkar"))

print("-" * 40)
print("{fname:>10} Tendulkar".format(fname="Sachin"))         # right alignment
print("{fname:^10} Tendulkar".format(fname="Sachin"))         # center alignment
print("{fname:<10} Tendulkar".format(fname="Sachin"))         # left alignment

print("{fname:*<10} Tendulkar".format(fname="Sachin"))
print("{fname:*^10} Tendulkar".format(fname="Sachin"))
print("{fname:*>10} Tendulkar".format(fname="Sachin"))

print("-" * 40)
from math import pi
print("{}".format(pi))
print("{:>010.2f}".format(pi))
print("{:^010.2f}".format(pi))
print("{:<010.2f}".format(pi))

print("Alignment".center(40, "-"))
print("{:-^40}".format("Alighment"))