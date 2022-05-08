class PlayerCharacter:
    def __init__(self, name, age):
        self.name = name #attributes
        self.age = age

    def run(self):
        return self # this is a way to find out what the self is

player1 = PlayerCharacter('andrei', 100)

print(player1.run()) # we are calling the run function to find out what the self method is