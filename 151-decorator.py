# Decorators

# @classmethod - is how a decorator looks like having an @
# @staticmethod

def hello(func):
   func()
    
def greet():
    print('still works')
    
a = hello(greet)
print(a)

# Decorator supercharge our functions
