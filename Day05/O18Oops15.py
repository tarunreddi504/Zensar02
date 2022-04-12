
# inheritance

class Animal:
    def __init__(self):
        print("Animal Ctor....")
        self.age = 1

    def eat(self):
        print("Animals eat.....")

class Bird(Animal):

    def fly(self):
        print("Birds fly.....")

class Fish(Animal):

    def swim(self):
        print("Fishes swim.....")

cuckoo = Bird()
cuckoo.fly()
cuckoo.eat()
print("-" * 40)

dolphin = Fish()
dolphin.swim()
dolphin.eat()
print("-" * 40)

print(cuckoo.__dict__)
print(dolphin.__dict__)
print("-" * 40)

print("isinstance(cuckoo, Bird) :", isinstance(cuckoo, Bird))
print("isinstance(cuckoo, Animal) :", isinstance(cuckoo, Animal))
print("isinstance(cuckoo, Fish) :", isinstance(cuckoo, Fish))
print("isinstance(cuckoo, object) :", isinstance(cuckoo, object))

print("-" * 40)
print("isinstance(dolphin, Fish) :", isinstance(dolphin, Fish))
print("isinstance(dolphin, Animal) :", isinstance(dolphin, Animal))
print("isinstance(dolphin, Bird) :", isinstance(dolphin, Bird))
print("isinstance(dolphin, object) :", isinstance(dolphin, object))
