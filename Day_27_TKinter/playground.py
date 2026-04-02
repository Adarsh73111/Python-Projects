# def add(*args):
#     print(args[1])
#     print(args)
#     print(type(args))
#     sum = 0
#     for n in args:
#         sum += n
#     return sum
#
# add(3, 5, 6)
# print(add(3,5,6,2,1,4,7,3))

# def calculate(n, **kwargs):
#     print(kwargs)
#     print(type(kwargs))
#     # for key, value in kwargs.items():
#     #     print(key)
#     #     print(value)
#     n+= kwargs["add"]
#     n*= kwargs["multiply"]
#     print(n)
#     # print(kwargs["add"])
# calculate(2, add=3, multiply=5)

class Car:

    def __init__(self, **kw):
        self.make  = kw.get("make")
        self.model = kw.get("model")
        self.color = kw.get("color")
        self.seats = kw.get("seats")

my_car = Car(make="Nissan", model="GT-R", color="Black", seats=2)
print(my_car.make)
print(my_car.model)
print(my_car.color)
print(my_car.seats)
