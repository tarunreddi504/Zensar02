
def funlogger(fnc):
    def helper(*args):
        print("Logged into the service...")
        print(fnc(*args))               # callback
        print("logged out of the service....")
        print("-" * 40)
    return helper

@funlogger
def add(x, y):
    print("add function called....")
    return x + y

@funlogger
def sub(x, y):
    print("sub function called.....")
    return x - y

@funlogger
def mul(x, y):
    print("multiply function called...")
    return x * y

add(345, 572)
sub(890, 530)
mul(12, 25)
