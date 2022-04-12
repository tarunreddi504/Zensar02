
def doubleMesh(fnc):
    def helper(*args):
        print("=" * 40)
        fnc(*args)
        print("#" * 40)
    return helper

def starSingle(fnc):
    def helper(*args):
        print("*" * 40)
        fnc(*args)
        print("-" * 40)
    return helper

@starSingle
@doubleMesh
def fun1():
    print("fun1 called......")

@starSingle
@doubleMesh
def fun2(x):
    print(f"fun2 called....:{x}")

@starSingle
@doubleMesh
def fun3(x, y):
    print(f"fun3 called......{x, y}")

@starSingle
@doubleMesh
def fun4(x, y, z):
    print(f"fun4 called.......{x, y, z}")

fun1()
fun2(10)
fun3(10, 20)
fun4(10, 20, 30)

