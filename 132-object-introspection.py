class User:
    def __init__(self, email): # a way to call this function is to call it under the Wizard class
        self.email = email

    def sign_in(self):
        print('logged in')

#    def attack(self):
#        print('do nothing')

class Wizard(User): #in this case we need to make sure that the Wizards and the Archers are all logged in by using the log in class
    def __init__(self, name, power, email): # we need to add the email in the function
#        User.__init__(self, email) # this is one way to do it
        super().__init__(email) # super coming from super class which means that is calling the class above "User" and we don't need to add self
        self.name = name
        self.power = power

    def attack(self):
#        User.attack(self) # using both wizard and user calling attack
        print(f'attacking with power of {self.power}')

# introspection --> the ability to determine the type of an object at run time is when the code is running to determine an object type when is running

wizard1 = Wizard('Merlin', 60, 'merlin@gmail.com') # and add the email in the call
print(dir(wizard1)) # with dir we can see to what our wizard method have access to what methods