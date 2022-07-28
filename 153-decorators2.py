# Decorators
# A decorator is a supercharge our function 
# Wrap our existing function and enhance it
 
def my_decorator(func):
    def wrap_func():
        print('************')
        func()
        print('""""""""""""""')
    return wrap_func

@my_decorator
def hello():
    print('heloooo')

@my_decorator
def bye():
    print('seee ya later')
    
hello()
bye()