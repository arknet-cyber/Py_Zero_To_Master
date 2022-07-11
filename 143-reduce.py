#reduce()
from functools import reduce

my_list = [1,2,3]

def accumulator(acc, item):
    print(acc, item)
    return acc + item

print(reduce(accumulator, my_list, 10)) # it is accumulating from my list + the value of the accumulator