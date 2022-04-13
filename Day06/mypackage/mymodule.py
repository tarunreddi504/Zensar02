
gname = "Sachin Tendulkar"

sports = ['cricket', 'tennis', 'soccer', 'hockey', 'basketball', 'swimming']

runs = {'odi': 28500, 'test': 21000, 't20': 2300}

# ------------------------------------------------------------

def greet(name):
    print(f"Greetings {name}, Welcome to the event")

def addMe(x, y):
    return x + y

#--------------------------------------------------------

class Players:

    def __init__(self, name, age):
        self.name = name
        self.age = age


    def get_details(self):
        print(f"Name = {self.name}\nAge = {self.age}")


