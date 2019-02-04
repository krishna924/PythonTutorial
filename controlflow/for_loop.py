

str = "Hello world is always boaring"

for  x in str:
    if x == 'a':
        print('A', end=' ')
    else:
        print(x, end=' ')

print('\n')
print('x'*30)
lst = ['one', 'two', 'three', 'four']

for l in lst:
    print(l)

print('x'*30)
mapex = {'one' : 1, 'two':2, 'three':3}
#print(mapex.items())
for x,y in mapex.items():
    # print('key is :' +x)
    # print('Value is :' +int(y))

    print("key is :"+x)
    print(y)


l1 = [1,2,3,4]
l2 = [5,6,7,8,8,1]

for a,b in zip(l1,l2):
    if a>b:
        print(a)
    else:
        print(b)