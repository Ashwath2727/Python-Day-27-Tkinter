def add(*args):
    print(args) #tuple
    sum = 0

    for num in args:
        sum += num

    return sum

def calculate(n, **kwargs):
    print(kwargs) #dictionary+

    n += kwargs["add"]
    n *= kwargs["multiply"]

    return n


print(add(45,46,23,123, 1, 2, 3, 4))

print(calculate(2, add=3, multiply=5))


class Car:

    def __init__(self, **kw):
        self.make = kw.get("make")
        self.model = kw.get("model")


my_car = Car(make="Ford")
print(my_car.make)
print(my_car.model)
