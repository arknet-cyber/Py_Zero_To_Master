# lambda expressions is a computer science term
# lambda is used  for one time use function

from functools import reduce

# lambda param: action(param)

my_list = [1,2,3]

def multiply_by2(item): #Because of the bellow lambda function we don't need this function in place if we are using lambda
    return item*2

def only_odd(item):
    return item % 2 != 0 #Because of the bellow lambda function we don't need this function in place if we are using lambda

def accumulator(acc, item):
    print(acc, item)
    return acc + item #Because of the bellow lambda function we don't need this function in place if we are using lambda

print(list(map(lambda item: item*2, my_list))) # lambda is going to get an item from "My_list" and multiply that item times 2
# lambda expressions are one time anonymous functions. There are no name attached to the above function that you don't need to run more than once
print(my_list)

# another example with filter

print(list(filter(lambda item: item % 2 != 0, my_list)))

print(reduce(lambda acc, item: acc+item, my_list))