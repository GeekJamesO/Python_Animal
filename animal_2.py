class Animal(object):
    def __init__(self, name, health):
        self.name = name
        self.health = health
    def walk(self):
        print "  {} is walking.".format(self.name)
        self.health -= 1
        return self
    def run(self):
        print "  {} is running.".format(self.name)
        self.health -= 5
        return self
    def displayHealth(self):
        print "  {} health = '{}'".format(self.name, self.health)
        return self

class Dog(Animal):
    def __init__(self, name, health=150):
        super(Dog, self).__init__(name, health)
    def pet(self):
        print "  The dog {} is getting petted.".format(self.name)
        self.health += 5
        return self


class Dragon(Animal):
    def __init__(self, name, health=170):
        super(Dragon, self).__init__(name, health)
    def fly(self):
        print "  The dragon {} is flying over its domain.".format(self.name)
        self.health -= 10
        return self
    def displayHealth(self):
        super(Dragon, self).displayHealth()
        print "  I am a Dragon!"
        return self

print "Animal tests:"
chuck = Animal("Chuck", 30)
chuck.displayHealth()
chuck.walk().walk().walk().run().run().displayHealth()

print "Dog tests:"
fido = Dog("Fido")
fido.displayHealth()
fido.walk().walk().walk().run().run().pet().displayHealth()

print "Dragon tests"
smug = Dragon("Smog")
smug.displayHealth()
smug.walk().walk().walk().run().run().fly().displayHealth()
print ' '
print "Tests that show that inherietance does works correctly."
print '--> chuck.pet()'
print '--> Traceback (most recent call last):'
print '-->   File "/Users/jamesorourke/Desktop/DojoAssignments/Python/Module2_Python_OOP/Animal/animal_2.py", line 54, in <module>'
print '-->     chuck.pet()'
print "--> AttributeError: 'Animal' object has no attribute 'pet'"
print ' '
print '--> chuck.fly()'
print '--> Traceback (most recent call last):'
print '-->   File "/Users/jamesorourke/Desktop/DojoAssignments/Python/Module2_Python_OOP/Animal/animal_2.py", line 60, in <module>'
print '-->     chuck.fly()'
print "--> AttributeError: 'Animal' object has no attribute 'fly' "
print ' '
print '--> fido.fly()'
print '--> Traceback (most recent call last):'
print '-->   File "/Users/jamesorourke/Desktop/DojoAssignments/Python/Module2_Python_OOP/Animal/animal_2.py", line 66, in <module>'
print '-->     fido.fly()'
print "--> AttributeError: 'Dog' object has no attribute 'fly' "
