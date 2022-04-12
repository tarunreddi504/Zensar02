
class Player:

    def __init__(self):
        self.name = "Sachin"                # instance variables
        self.age = 36
        print("player Initialized......")

    def get_details(self):
        print(f"name ={self.name}\nAge = {self.age}")

    def __del__(self):
        print("destructor called...")

ply1 = Player()                 # memory will be allocated to the object
ply1.get_details()

del ply1                        # calls the destructor and release the memory consumed by the object

print("-" * 40)
ply2 = Player()
ply2.name = "Rahul"
ply2.age = 32
ply2.get_details()

print("-" * 40)