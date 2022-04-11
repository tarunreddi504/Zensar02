
glbx = 100

def fun(n):                     # local variable, will be declared in the function stack
    print(n)
    glbx = 500                  # local variable with same name as global variable
    print(f"glbx Inside :{glbx}")


print(f"glbx Before :{glbx}")

fun(50)

# print(f"n :{n}")                  local variables declared inside the function is not accessible outside the function

print(f"glbx After :{glbx}")
