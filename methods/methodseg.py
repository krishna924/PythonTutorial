

def sumof (a1, a2):
    print(a1 + a2)

sumof(1,2)
sumof(3,5)

def sum_num (b1, b2):
    """
    Sum of two numbers
    :param b1:
    :param b2:
    :return:
    """
    return b1+b2

a = sum_num(1,2)
b = sum_num('aaple', 'green')
print(a)
print(b)

print('**'*20)

def isMetra(m1):
    """
    Get if a city is metra or not
    :param m1:
    :return:
    """
    l1 = ['sfo', 'chicago', 'dal', 'austin']

    if m1 in l1 :
        return True
    else:
        return False

c = isMetra('sfo')
d = isMetra('new york')
print(c)
print(d)


def sum_num1 (b1 = 2, b2 = 3):
    """
    Sum of two numbers
    :param b1:
    :param b2:
    :return:
    """
    return b1+b2

a1 = sum_num1(1,2)
a2 = sum_num1()

print(a1)
print(a2)

# Global variable example
x = 10

def printing_vaalue (x1):

    global x
    print("glovbal value" + str(x))
    x = 2
    print("changed global vlue" + str(x))

print("actual value" + str(x))
printing_vaalue(1)
print("changed value" + str(x))
