
def outerFun(gname):
    guest = f"Mr.{gname}"

    def innerFun():
        print(f"Hello {guest}")

    return innerFun

outerFun("Sachin")()                # calls the innerFun

print("-" * 40)
inrFun = outerFun("Rahul")
inrFun()

print("-" * 40)
print(outerFun.__name__)
print(outerFun("Sehwag").__name__)

print("-" * 40)
inrFun = outerFun("Dhoni")

print("Before the inner funtion call")
inrFun()