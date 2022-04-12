
class Player:                   # pascal casing

    def get_runs(self):         # self is used in all methods of a class, self is like this pointer
        print("runs scored......")

sachin = Player()
print(type(sachin))
sachin.get_runs()

print(isinstance(sachin, Player))
print(isinstance(sachin, object))
print(isinstance(sachin, str))

# object is the base class of all classes
