
"""
st is an object str class
str - methods -> to manipulate a string

"""
# convert the string into upper case
print("upper".center(40, "-"))
st = "hello world"
print(f"st :{st}")
res = st.upper()
print(f"res :{res}")

print("-" * 40)
st = "Hello World"
print(f"st :{st}")
res1 = st.find("l")
print(f"res1 :{res1}")

res2 = st.find("l", 4)
print(f"res2 :{res2}")

res3 = st.find("z")
print(f"res3 :{res3}")

st = "the quick brown fox jumps  over the lazy dog"
print(f"st :{st}")
res4 = st.find("the")
print(f"res4 :{res4}")

res5  = st.find("the", 3)
print(f"res5 :{res5}")

print("replace".center(40, "-"))
st = "hello world"
print(f"st :{st}")
res1 = st.replace("h", "H")
print(f"res1 :{res1}")

print("-" * 40)
res2 = st.replace("l", "L",1)
print(f"res2 :{res2}")              # dictionary with ascii values

# maketrans, translate
print("maketrans".center(40, "-"))
st = "hello world"
print(f"st :st")
a = "helowrd"
b = "HELOWRD"
# the number of characters in a and b should be the same
resTbl = st.maketrans(a, b)
print(f"resTbl :{resTbl}")

print("translate".center(40, "-"))
print(f"st :{st}")
res = st.translate(resTbl)
print(f"res :{res}")

print("strip".center(40, "-"))
st= "******hello********"

res1 = st.rstrip("*")
print(f"res1 :{res1}")

res2 = st.lstrip("*")
print(f"res2 :{res2}")

res3 = st.strip("*")
print(f"res3 :{res3}")

print("zfill".center(40, "-"))
n = "50"
st = "hello world"
print(f"n :{n}")
print(f"st :{st}")

# zfill
print(n.zfill(10))
print(st.zfill(15))