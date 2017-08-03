# Assignment: Animal
# Create an Animal class and give it the below attributes and methods. Extend the
# Animal class to two child classes, Dog and Dragon.
#
# Objective
# The objective of this assignment is to help you understand inheritance.
# Remember that a class is more than just a collection of properties and methods.
# If you want to create a new class with attributes and methods that are already
# defined in another class, you can have this new class inherit from that other
# class (called the parent) instead of copying and pasting code from the original class.
# Child classes can access all the attributes and methods of a parent class AND
# have new attributes and methods of its own, for child instances to call. As we
# see with Wizard / Ninja / Samurai (that are each descended from Human), we can
# have numerous unique child classes that inherit from the same parent class.
#
# Animal Class
# Attributes:
#    name
#    health
# Methods:
#    walk: decreases health by one
#    run: health decreases by five
#    display health: print to the terminal the animal's health.

class Animal(object):
    def __init__(self, name, health):
        self.name = name
        self.health = health
    def walk(self):
        self.health -= 1
        return self
    def run(self):
        self.health -= 5
        return self
    def displayHealth(self):
        print "  {0}  {1}".format(self.name, self.health)
        return self
# Create an instance of the Animal, have it walk() three times, run() twice, and
# finally displayHealth() to confirm that the health attribute has changed.
#
# Dog Class
#    inherits everything from Animal
# Attributes:
#    default health of 150
# Methods:
#    pet: increases health by 5

class Dog(Animal):
    def __init__(self, name, health=150):
        super(Dog, self).__init__(name, health)
    def pet(self):
        self.health += 5
        return self

# Have the Dog walk() three times, run() twice, pet() once, and have it displayHealth().
print "Taking Fido out for a bit."
dog1 = Dog("Fido")
dog1.walk().walk().walk().run().run().pet().displayHealth()
print ""
#
# Dragon Class
#    inherits everything from Animal
# Attributes:
#    default health of 170
# Methods:
#    fly: decreases health by 10
#    display health: prints health by calling the parent method and prints "I am a Dragon"
class Dragon(Animal):
    def __init__(self, name, health=170):
        super(Dragon, self).__init__(name, health)
    def fly(self):
        self.health -= 10
        return self
    def displayHealth(self):
        super(Dragon, self).displayHealth()
        print "  I am a Dragon"
        return self
print "Taking the black dragon out for a bit."
dragon1 = Dragon("Toothless")
dragon1.walk().fly().displayHealth()
print ""

# Now try creating a new Animal and confirm that it can not call the pet() and
# fly() methods, and its displayHealth() is not saying 'this is a dragon!'.
# Also confirm that your Dog class can not fly().

# lucky = Dog("Lucky")
# lucky.fly()
"""
    File "/Users/jamesorourke/Desktop/DojoAssignments/Python/animal/animal.py", line 88, in <module>
        lucky.fly()
    AttributeError: 'Dog' object has no attribute 'fly'
"""

RedDragon = Dragon("Mr. Angry")
RedDragon.pet()
"""
      File "/Users/jamesorourke/Desktop/DojoAssignments/Python/animal/animal.py", line 96, in <module>
        RedDragon.pet()
    AttributeError: 'Dragon' object has no attribute 'pet'
"""
