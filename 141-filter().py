 # filter()

my_list = [1,2,3,5,6,10,11,14]
def multiply_by2(item):
    return item*2

def only_odd(item):
    return item % 2 != 0 # this will evaluate in a boolean value

print(list(filter(only_odd, my_list))) #here the filter  is using the only_odd function to go through the above list
#print(my_list)

# my example