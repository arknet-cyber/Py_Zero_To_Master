# *args and **kwargs

def super_func(*args): #by providing a start that means that can accept any positional arguments
    print(args)
    return sum(args)

super_func(1,2,3,4,5)
print(super_func(1,2,3,4,5))



def super_func(*args, **kwargs): #by providing a start that means that can accept any positional arguments
    total = 0
    for items in kwargs.values():
        total += items
    return sum(args) + total

print(super_func(1,2,3,4,5, num1=5, num2=10))