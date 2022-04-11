
"""
outerFun is the parent of innerFun
to declare a nonlocal variable we should have it as a local variable in the parent function
"""

gstname = "Sourav"

def outerFun():
    # global gstname
    gstname = "Sachin"              # local variable for outerFun

    def innerFun():
        global gstname
        gstname = "Rahul"           # local variable for innerFun
        print(f"Hello {gstname}")

    print(f"Before :{gstname}")         # local variable of outerFun
    innerFun()                          # call to innerFun from outerFun
    print(f"After :{gstname}")

print(f"Before Outer:{gstname}")
outerFun()
print(f"After Outer :{gstname}")