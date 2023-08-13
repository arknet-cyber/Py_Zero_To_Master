# Files I/O

my_file = open('185-filetest.txt')

print(my_file.read())
my_file.seek(0)
print(my_file.read())
print(my_file.readline())
print(my_file.readlines())

my_file.close()