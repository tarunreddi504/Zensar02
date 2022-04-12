
class Player:

    def __init__(self, name, age):
        self.name = name
        self.age = age
        print("Player Initialized.....")

    def get_details(self):
        print(f"Name ={self.name}\nAge = {self.age}")

ply1 = Player("Dhoni", 38)
ply1.get_details()              # obj.method()      => self will store the name of the object

print("-" * 40)

ply2 = Player("Virat", 33)
ply2.get_details()

print("-" * 40)
print(ply1.__dict__)            # instance variables of ply1

print("-" * 40)
print(ply2.__dict__)            # instance variables of ply2

print("-" * 40)
ply2.runs = 250

print("-" * 40)
print("ply1 :", ply1.__dict__)
print("ply2 :", ply2.__dict__)

