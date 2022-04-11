
def bank_flow(fnc):                 # HOF
    print("-" * 40)
    print("login")
    fnc()
    print("logout")
    print("-" * 40)

def withdraw():
    print("debitted.....")

def deposit():
    print("creditted.....")

def gift():
    print("transferred......")

bank_flow(withdraw)
bank_flow(deposit)
bank_flow(gift)
