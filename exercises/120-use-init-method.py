#Given the below class:
class Cat:
    species = 'mammal'
    def __init__(self, name, age):
        self.name = name
        self.age = age


# 1 Instantiate the Cat object with 3 cats

peanut = Cat('Peanut', 10)
garfield = Cat('Garfield', 14)
snickers = Cat('Snickers', 16)

# 2 Create a function that finds the oldest cat

def get_oldest_cat(*args):
    return max(args)

# 3 Print out: "The oldest cat is x years old.". x will be the oldest cat age by using the function in #2
print(f"The oldest cat is {get_oldest_cat(peanut.age, garfield.age, snickers.age)} years old")