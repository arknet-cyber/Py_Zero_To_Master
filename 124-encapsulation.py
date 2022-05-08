class PlayerCharacter:
    def __init__(self, name, age):
        self.name = name #attributes
        self.age = age

    def run(self):
        print('run')

    def speak(self):
        print(f'my name is {self.name} and age is {self.age} years old')

# The above is an entire object which is encapsulated and we can use 

player1 = PlayerCharacter('andrei', 100)
player1.speak()