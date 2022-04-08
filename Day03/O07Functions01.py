

def greet():
    print("Welcome Mr. Sachin Tendulkar to the event....")

def greetGuest(gstName):
    print(f"Welcome Mr.{gstName} to the event....")

# gstName - non default argument, city - default argument
def GreetGuestCity(gstName, city="Mumbai"):
    print(f"Welcome Mr. {gstName} from {city} to the event....")

greet()
print("-" * 40)
greetGuest("Rahul Dravid")
greetGuest("Sourav Ganguly")
print("-" * 40)
GreetGuestCity("Sachin")
GreetGuestCity("Rohit")
GreetGuestCity("Dhoni", "Ranchi")

print("-" * 40)

def enroll(fname, lname, dob, qlf, cno, adr, adhrno):
    print(fname, lname, dob, qlf, cno, adr, adhrno)

# named arguments
enroll(dob="12/10/1987", lname="kholi", fname="virat", qlf='Btech',  adhrno=3564545, cno=456323423, adr="sdfsdfsdf")

print("-" * 40)

def multiplyMe(x, y):
    return x * y
    print("function code executed successfully....")


print(f"The product of 10 and 20 is {multiplyMe(10, 20)}")

# print("-" * 40)
# def auto_greet():
#     return("Greetings, Welcome to the event, have a great day")
#
# print(auto_greet())

# recursive call
def fun(n):
    print(n, end=' ')
    if n == 1:
        return 1
    fun(n - 1)

fun(10)
print()
print("-" * 40)

# how many arguments can a function return
def arithematicCalc(x, y):
    sum = x + y
    diff = x - y
    prod = x * y
    quot = x / y
    return sum, diff, prod, quot

res = arithematicCalc(20, 8)            # res = 28, 12, 160, 2.5
print(f'res :{res}')

print("-" * 40)
# variable length arguments
# *args, **kwargs

def productAll(*numbers):       # arguments like tuple
    print(f"numbers :{numbers}")
    print(f"numbers :", *numbers)           # unpacking and printing
    prod = 1
    for num in numbers:
        prod *= num         # prod = prod * num
    return prod

print("Multiply All =", productAll(1, 2, 3, 4, 5))

print("-" * 40)
def extract_details(**detail):
    print(detail)
    print(detail['name'])
    print(detail['oponent'])


extract_details(name="Sachin", score=185, oponent="ENG")

# doc strings

def fun():
    # this is a comment
    "this is a doc string"

    print("hello world")

print("-" * 40)
fun()
print(fun.__doc__)              # docstring

print("-" * 40)

def fun1(x, y):
    """
    funtion fun1 takes two argument x and y
    x is the first argument of type integer
    y is the second argument of type integer

    int = fun1(x, y)

    the return value of the funtion is of type integer
    and it will be the sum of x and y
    """

    return x + y

res = fun1(10, 20)
print(f"res :{res}")

print("-" * 40)
help(fun1)