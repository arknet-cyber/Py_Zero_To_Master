# When you see an underscore in the variable, that means you should not touch the variable is how you achieve privacy in python
class PlayerCharacter:
    def __init__(self, name, age):
        self._name = name #attributes
        self._age = age # if you see an underscore you should not modify this

    def run(self):
        print('run')

    def speak(self):
        print(f'my name is {self._name} and age is {self._age} years old')

# The above is an entire object which is encapsulated and we can use 

player1 = PlayerCharacter('andrei', 100)
print(player1.speak())