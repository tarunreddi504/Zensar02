
# c style formatting
format = "Welcome %s, what a %s player"
print(format)
values = ("Sachin", "superb")
print(values)

print(format % values)
print("-" * 40)

format = "Welcome %s, Your rating of %.3f, what a player"
print(format % ("Sachin", 4))
print(format % ("Sachin", 4.2))
print(format % ("Sachin", 4.223345))
print(format % ("Sachin", 4.2787729))
print("-" * 40)
print("Welcome %s, your rating of %.3f, what a player" % ("Sachin", 4))
print("-" * 40)

# unix shell syntax
from string import Template
tmpl = Template("Welcome $name, what a $adjective player")
print(f"tmpl :{tmpl}")
res = tmpl.substitute(name="Sachin", adjective="super")
print(res)

# format strings from python
print("-" * 40)
print("Welcome {}, what a {} player for {}".format("Sachin", "superb", "India"))
print("Welcome {0}, what a {1} player for {2}".format("Sachin", "Super", "India"))
print("Welcome {gname}, what a {adj} player for {cntry}".format(gname="Sachin", adj="superb", cntry="India"))
print("Welcome {name}, Your rating of {rating}, what a player".format(name="Sachin", rating=4))
print("Welcome {name}, Your rating of {rating:.3f}, what a player".format(name="Sachin", rating=4))

# interpolation
from math import pi, e
print(f"PI = {pi} and Eulers constant = {e}")

print("PI = {} and Eulers constant = {}".format(pi, e))
print("PI = {0} and Eulers constant = {1} and magic number = {2}".format(pi, e, 40585))
print("PI = {} and Eulers constant = {} and magic number = {magic}".format(pi, e, magic=40585))
print("PI = {0} and Eulers constant = {1} and magic number = {magic}".format(pi, e, magic=40585))

print("-" * 40)
fullname = ["Sachin", "Tendulkar"]
print(f"fullname :{fullname}")
print("Mr.{name}".format(name=fullname))
print("Mr.{name[0]}".format(name=fullname))
print("Mr.{name[1]}".format(name=fullname))

print("-" * 40)
import math
print(__name__)             # double underscore name => dunder name
print(math.__name__)

print("The {mod.__name__} module gives the value of pi= {mod.pi} and eulers= {mod.e}".format(mod=math))
