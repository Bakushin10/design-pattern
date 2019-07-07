"""
https://github.com/faif/python-patterns/blob/master/patterns/creational/abstract_factory.py
"""

import random

class PetShop(object):

    def __init__(self, animal_factory = None):
        self.pet_factory = animal_factory
    
    def show_pet(self):
        pet = self.pet_factory()
        print("We have a lovely {}".format(pet))
        print("It says {}".format(pet.speak()))
    

class Dog(object):
    def speak(self):
        return "woof"
    
    def __str__(self):
        return "Dog"

class Cat(object):
    def speak(self):
        return "meow"
    
    def __str__(self):
        return "Cat"

def random_animal():
    return random.choice([Dog, Cat])()

if __name__ == "__main__":
    cat_shop = PetShop(Cat)
    cat_shop.show_pet()

    shop = PetShop(random_animal)
    for i in range(3):
        shop.show_pet()
        print("=" * 20)

