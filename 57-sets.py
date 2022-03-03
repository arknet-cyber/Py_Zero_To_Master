# Sets are unordered collection of unique objects

my_set = {1,2,3,4,5,5} # this look like a dictionary but is a Sets
print('If we print this sets my_set = {1,2,3,4,5,5} will give use only the unique objects')
print(my_set)
my_set.add(100)
my_set.add(2)
print(my_set)


# My exercise
print('My own exercise')
print()
my_list = [1,2,3,4,5,5]
print()
print('We need to convert it to set')
print('print(set(my_list))')
print(set(my_list))

my_super_set = {1,2,3,4,5,5}
#print(list(my_super_set) # Converting the sets into a list)
new_set = my_super_set.copy()
print(new_set)
print(my_super_set)