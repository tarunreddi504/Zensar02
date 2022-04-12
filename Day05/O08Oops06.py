
class Player:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def get_details(self):
        print(f"Name = {self.name}\nAge = {self.age}")

    @classmethod
    def CreatePlayer(cls, fname, lname, age):                  # factory
        print("factory")
        return cls(f"Mr. {fname} {lname}", age)

ply1 = Player("Kholi", 33)
ply1.get_details()

print("-" * 40)
ply2 = Player.CreatePlayer("Sachin", "Tendulkar", 38)
ply2.get_details()