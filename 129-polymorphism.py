# Referres to the way in which an object class can share the same method name

class User:
    def sign_in(self):
        print('logged in')

    def attack(self):
        print('do nothing')

class Wizard(User): #in this case we need to make sure that the Wizards and the Archers are all logged in by using the log in class
    def __init__(self, name, power):
        self.name = name
        self.power = power

    def attack(self):
        User.attack(self) # using both wizard and user calling attack
        print(f'attacking with power of {self.power}')

class Archer(User):
    def __init__(self, name, num_arrows):
        self.name = name
        self.num_arrows = num_arrows

    def attack(self):
        print(f'attacking with arrows: arrows left- {self.num_arrows}')


wizard1 = Wizard('Merlin', 50)
archer1 = Archer('Robin', 100)
wizard1.attack()
archer1.attack()

print(isinstance(wizard1, User)) #the result inherits from wizard class from the user class and from the object base class that python come with 
#print(wizard1.sign_in()) # we are calling the sing in function from the User's class, so we inherited

print()
print('This is a way to demonstrate polymorphism')

def player_attack(char): 
    char.attack()

player_attack(wizard1) # this is polymorphism that we are passing different object regardless the above function
player_attack(archer1)

# Another way to do this:
for char in [wizard1, archer1]:
    char.attack()