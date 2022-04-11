
glbx = 100

def fun(n):                     # local variable
    global glbx                 # cannot assign a value to the variable\
    glbx = 250                  # global variable
    print(n)
    # glbx = 500                  # local variable with same name as global variable
    print(f"glbx Inside :{glbx}")


print(f"glbx Before :{glbx}")

fun(50)

print(f"glbx After :{glbx}")
