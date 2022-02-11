# Tuples are imutable we can't change values in the tuple

my_tuple = (1,2,3,4,5)
new_tuple = my_tuple[1:4]

print(my_tuple.count(5))
print(my_tuple.index(5))
print(len(my_tuple))
print(new_tuple)

x,y,z, *other = (1,2,3,4,5)
print(x)
print(y)
print(z)
print(other)