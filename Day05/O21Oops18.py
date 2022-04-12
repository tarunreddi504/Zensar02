
class Animal:
    def __init__(self):
        print("Animal Ctor......")
        self.a = 10

    def eat(self):
        print("Animals eat.....")

    def fun(self):
        print("fun method of Animal class.....")

class Person:
    def __init__(self):
        print("Person Ctor......")
        self.p = 20

    def talk(self):
        print("person talks")

    def fun(self):
        print("fun method of Person class.....")

class Girl(Animal, Person):
    def __init__(self):
        super().__init__()
        Person.__init__(self)
        self.g = 30
        print("Girl Ctor........")

gracy = Girl()
print("-" * 40)
gracy.talk()
gracy.eat()


print("-" * 40)
gracy.fun()
print(gracy.__dict__)