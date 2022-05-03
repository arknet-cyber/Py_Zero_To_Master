class PlayerCharacter:
    # Class Object Attribute
    membership = True
    def __init__(self, name='anonymous', age=0):
        if (age > 18):
            self.name = name #attributes
            self.age = age

    def shout(self):
        print(f'my name is {self.name}')
        #return 'done'

player1 = PlayerCharacter('Tom', 10)


print(player1.shout())