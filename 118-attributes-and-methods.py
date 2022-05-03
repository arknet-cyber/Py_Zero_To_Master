class PlayerCharacter:
    # Class Object Attribute
    membership = True
    def __init__(self, name, age):
        if (PlayerCharacter.membership):
            self.name = name #attributes
            self.age = age

    def shout(self):
        print(f'my name is {self.name}')
        #return 'done'

player1 = PlayerCharacter('Cindy', 44)
player2 = PlayerCharacter('Tom', 21)
player2.attack = 50

#print(player1.shout())
#print(player2.shout())

help(player1)