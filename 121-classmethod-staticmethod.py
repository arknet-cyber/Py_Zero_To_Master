class PlayerCharacter:
    membership = True
    def __init__(self, name, age):
        self.name = name #attributes
        self.age = age

    def shout(self):
        print(f'my name is {self.name}')

# This is a class method and in the class methods we care about the above class attributes
    @classmethod
    def adding_things(cls, num1, num2): # cls stands for class
        return cls('Teddy', num1 + num2)

# This is a static method and the difference is that we don't have the "cls" like in the @classmethod
# And also we don't care about the class attributes

    @staticmethod
    def adding_things(num1, num2):
        return (num1 + num2)

# player1 = PlayerCharacter('Cindy', 44)
player3 = PlayerCharacter.adding_things(2,3)
#print(PlayerCharacter.adding_things(2,3))
print(player3.age)