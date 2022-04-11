
def funLogger(fnc):
    def helper():
        print("My info logged in a service....")
        fnc()
        print("My info logged out of the service......")
    return helper

def normalFun():
    print("I should call as normal.....")

funLogger(normalFun)                # NO OUTPUT
print("-" * 40)
funLogger(normalFun)()
print("-" * 40)
res_fun = funLogger(normalFun)
res_fun()

print("-" * 40)
@funLogger                      # decorator
def basicFun():
    print("I should be called as Basic....")

# basicFun = funLogger(basicFun)
# basicFun()

basicFun()
basicFun()