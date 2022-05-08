# Inheritance allow new object to take on the properties of an existing object

class User:
    def sign_in(self):
        print('logged in')

class Wizard(User): #in this case we need to make sure that the Wizards and the Archers are all logged in by using the log in class
    def __init__(self, name, power):
        self.name = name
        self.power = power

    def attack(self):
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
wizard1.__repr__
print(isinstance(wizard1, User)) #the result inherits from wizard class from the user class and from the object base class that python come with 
#print(wizard1.sign_in()) # we are calling the sing in function from the User's class, so we inherited