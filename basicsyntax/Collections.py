from builtins import print

cars = ["benz", "bmw", "mazda"]
print(cars)
print(cars[1])
cars[2] = "audi"
print(cars)
print("*#"*20)

# default methods to manipulate lists

lenght = len(cars)
print(lenght)

cars.append("honda")
print(cars)

cars.insert(2,"mazda")
print(cars)

print(cars.index("honda"))

cars.pop(1)
print(cars)

cars.remove("honda")
print(cars)

slicing = cars[0:2]
print(slicing)

cars.sort()
print(cars)