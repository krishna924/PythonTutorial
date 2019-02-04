
a = " this is an example"
b = 'this is a simple quote'
c = "hello worls give me \"quotes\""
d = "hello there \
this is a single string "

print(a)
print(b)
print(c)
print(d)

print("****************************************************")

first = "nyc"[0]
city = "chicago"
ab = city[1]
print(ab)
print(first)

"""
common used methods in string
len()
lower()
upper()
str()
"""

str1 = "Hello"
print(str1 + " " +str(222))


print("*******************************************")

# sub string methods
a1 = "1abc2abc3abc4abc"
print(a1.replace('abc','ABC'))
sub = a1[1:6]
step = a1[1:6:2]

print(sub)
print(step)


# Formatting the screan

city = 'nyc'
event = 'musical show'
print("welcome to the %s. Enjoy the %s" %(city, event))