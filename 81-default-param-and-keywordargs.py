# parametres

def say_hello(name, emoji): # this are the variable of the function called parametres
    print(f'hello {name} {emoji}')

# positional argument are arguments which require to be in a specific position

say_hello('Andrei', ':P')
say_hello('Juls', ':P')
say_hello('Naz', ':P')

# keywords arguments

say_hello(emoji=':P', name='Bibi')

# Default parametres are those parameters who are defined in the function and when the function is called withut arguments will display the default ones

def cars(name='Tesla', color='white'):
    print(f'You have a nice {color} {name}')

cars()