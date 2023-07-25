# Generators are very good becasue they don't use the in-memory 

#range(100) # range it creates the range of numers on by one without using the in-memory
#list(range(100)) # we convert here the range into the list where we need to wait for the rnge of numbers to be created and push it to the memeory to make use of it

def make_list(num):
    result = []
    for i in range(num):
        result.append(i*2)
    return result

my_list = make_list(100)
print(my_list) 