
class Product:

    def __init__(self, price):
        self.__price = price

    @property
    def price(self):
        print("getter called.....")
        return f"The price is {self.__price}"

    @price.setter
    def price(self, val):
        print("setter called.....")
        self.__price = val

    @price.deleter
    def price(self):
        print("deleter called....")
        self.__price = 0


sprite = Product(50)
print(sprite.price)
sprite.price = 85
print(sprite.price)

del sprite.price
print(sprite.price)
