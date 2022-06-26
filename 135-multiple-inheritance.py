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
    def __init__(self, name, arrows):
        self.name = name
        self.arrows = arrows

    def check_arrows(self):
        print(f'{self.arrows} remaining')

    def run(self):
        print('ran really fast')

# Here is where the multiple inheritance
class HybridBorg(Wizard, Archer):
    def __init__(self, name, power, arrows):
        Archer.__init__(self, name, arrows)
        Wizard.__init__(self, power, power)

hb1 = HybridBorg('borgie', 50, 100)
print(hb1.attack())