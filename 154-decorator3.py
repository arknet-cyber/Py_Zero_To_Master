# Decorators
# A decorator is a supercharge our function 
# Wrap our existing function and enhance it
 
def my_decorator(func):
    def wrap_func(x, y):
        print('************')
        func(x, y)
        print('""""""""""""""')
    return wrap_func

@my_decorator
def hello(greeting, emoji):
    print(greeting, emoji)

hello('heeee', ':)')


# Another way to do it is when we have a 
# Decorator patern

def my_decorator(func):
    def wrap_func(*args, **kwargs): # this is useful becasue we dont need to change all the time key values
        print('************')
        func(*args, **kwargs)
        print('""""""""""""""')
    return wrap_func

@my_decorator
def hello(greeting, emoji=':('):
    print(greeting, emoji)

hello('heeee')