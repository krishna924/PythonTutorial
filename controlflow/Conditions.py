"""
if
while
for
"""

a = 100
b = 10

if a > b :
    print("a is greater than b")

elif a == b:
    print("a is equal to b")

else:
    print("Thats how it is")


# while

x = 0
num = []
while x < 10:
    num.append(x)
    x += 1
print(num)


z = 0

# while z <= 10:
#     print("the value of string is :" + str(z))
#     z += 1
#
#     if z == 8:
#         break
#     print("awesome")
#     print("*"*24)
#
# else:
#     print("Break out of the loop")



while z <= 10:
    print("the value of string is :" + str(z))
    z += 1

    if z == 8:
        continue
    print("awesome")
    print("*"*24)

else:
    print("Break out of the loop")
