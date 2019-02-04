"""
File I/O
'w' -> Write only mode
'r' -> read only
'r+' -> Read and Write
'a' -> append mode
"""

list = [1,2,3,4]

file = open('firstfile.txt', 'w')

for l in list :
    file.write(str(l) + "\n")

file.close()

"""
Reading a file -> .read()
Reading a file line by line -> .readline() 
"""

my_file = open('firstfile.txt', 'r')
print(str(my_file.read()))
my_file.close()
print('Line by Line ============================>')

my_file = open('firstfile.txt', 'r')
print(str(my_file.readline()))
print(str(my_file.readline()))
print(str(my_file.readline()))
my_file.close()


print("With write as start")
with open("withas.txt", "w") as  wiith_as_write:
    wiith_as_write.write("This is an example of write/read")

print()
print("Whith as read start")

with open("withas.txt", "r") as wiith_as_read:
    print(str(wiith_as_read.read()))