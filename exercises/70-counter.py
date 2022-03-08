# counter
my_list = [1,2,3,4,5,6,7,8,9,10]

def sum_of_list(l):
    total = 0
    for val in l:
        total = total + val
    return total

print('The sum of my list is ', sum_of_list(my_list))

# the tutor answer
counter = 0
for item in my_list:
    counter = counter +item
    
print(counter)