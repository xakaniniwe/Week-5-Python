Polymorphism Challenge
class Animal:
    """
    Base class for animals with a generic move action.
    """
    def __init__(self, name):
        self.name = name

    def move(self):
        """
        Generic move action - to be overridden by subclasses.
        """
        print(f"{self.name} makes a general movement.")

class Dog(Animal):
    """
    Represents a dog with a specific move action.
    """
    def move(self):
        print(f"{self.name} is running.")

class Cat(Animal):
    """
    Represents a cat with a specific move action.
    """
    def move(self):
        print(f"{self.name} is prowling.")

class Bird(Animal):
    """
    Represents a bird with a specific move action.
    """
    def move(self):
        print(f"{self.name} is flying.")

# Creating instances of different animal types
dog = Dog("Buddy")
cat = Cat("Whiskers")
bird = Bird("Tweety")

# Calling the move() method on each object
animals = [dog, cat, bird]
for animal in animals:
    animal.move()