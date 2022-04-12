
class Players:

    def __init__(self, name, age):
        self.name = name
        self.age = age

    def __str__(self):
        return f"Name = {self.name}\nAge = {self.age}"

ply1 = Players("Sourav", 35)
print(str(ply1))                # calls __str__()
print("-" * 40)
print(ply1.__str__())

print("-" * 40)
print(ply1)                     # implicitly calls __str__

