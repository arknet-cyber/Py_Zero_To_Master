# Tuples are immutable we can't change values in the tuple

my_tuple = (1,2,3,4,5)
print(5 in my_tuple)

user = {
  (1,2): [1,2,3],
  'greet': 'hello',
  'age': 55
}

print(user[(1,2)]) # We accessing the key in the tuple inside the dictionary


my_tuple = (1,2,3,4,5)
my_tuple[1] = 'z'