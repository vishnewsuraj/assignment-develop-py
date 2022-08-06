'''
''''''''''''''''''''''''''
OOPs concepts
''''''''''''''''''''''''''
'''

# class
class Parrot:
    pass


# Object

class Person:
    species = 'Work feedback'
    def __init__(self, name, designation):
        self.name = name
        self.designation = designation

# instantiate the Parrot class
personObjOne = Person("Suraj", "Backend Developer")
personObjTwo = Person("Roman", "Frontend Developer")

# access the class attributes
print("Backend developer is {}: ".format(personObjOne.__class__.species))
print("Frontend developer is {}: ".format(personObjTwo.__class__.species))

# access the instance attributes
print("Name is {0} and designation is {1} ".format(personObjOne.name, personObjOne.designation))
print("Name is {0} and designation is {1} ".format(personObjTwo.name, personObjTwo.designation))


# Creating Method

class Parrot:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def sing(self, song):
        return '{} sings {}'.format(self.name, song)
    def dance(self):
        return '{} is now dancing'.format(self.name)

blu = Parrot('Blu', 10)
print(blu.sing("Happy"))
print(blu.dance())



# Inheritance

# Parent class

class Bird:
    def __init__(self):
        print("Bird is ready")

    def whoIsThis(self):
        print("Bird")

    def swim(self):
        print("Swim faster")


# child class
class Penguin(Bird):

    def __init__(self):
        # call super() function
        super().__init__()
        print('Penguin is ready')

    def whoIsThis(self):
        print('Penguin')

    def run(self):
        print('Run faster')

peggy = Penguin()
peggy.whoIsThis()
peggy.swim()
peggy.run()



# Data Encapsulation in Python

class Computer:

    def __init__(self):
        self.__maxPrice = 711

    def sell(self):
        print("Selling Price : {}".format(self.__maxPrice))

    def setMaxPrice(self, price):
        self.__maxPrice = price

c = Computer()
c.sell()

# change the price
c.__maxPrice = 1000
c.sell()

# using setter function
c.setMaxPrice(1000)
c.sell()


# Polymorphism

class Parrot:

    def fly(self):
        print("Parrot can fly")

    def swim(self):
        print("Parrot can't swim")


class Penguin:

    def fly(self):
        print("Penguin can't fly")

    def swim(self):
        print("Penguin can swim")


# common interface
def flying_test(bird):
    bird.fly()


# instantiate objects
blu = Parrot()
peggy = Penguin()

# passing the object
flying_test(blu)
flying_test(peggy)