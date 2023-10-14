#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Oct 13 14:41:26 2023

@author: monika
"""
import random

# Defining a Class (Recap) with an example of class Animal
# Subclass : Hierarchy in classes


class Animal(object):
    def __init__(self, age):
        self.age = age
        self.name = None
    def get_age(self):
        return self.age
    def get_name(self):
        return self.name
    def set_age(self, newage):
        self.age = newage
    def set_name(self, newname = ""):
        self.name = newname
    def __str__(self):   
        return "animal:" + str(self.name) + ":" + str(self.age)

myAnimal = Animal(3)
print("myAnimal =", myAnimal)

myAnimal.set_name("foobear")
print("myAnimal =", myAnimal)
print("myAnimal.get_age() =", myAnimal.get_age())
print("Animal.get_age(myAnimal) =", Animal.get_age(myAnimal)) # same as above

print("myAnimal.age =", myAnimal.age) # same as above BUT directly access the data should be avoided as:
    # using GETTERS outside of instances to get out the internal info pieces IS PREFERRED.
    # If you're doing data access directly outside of the class and the class definition changes,
    # you can get errors.
print("____________")
print()



# Creating subclasses like Cat, Rabbit, Person from parent class Animal

# Subclass Cat
class Cat(Animal):
    def speak(self):
        print("meow")
    def __str__(self):
        return "cat:" + str(self.name) + ":" + str(self.age)

jelly = Cat(1)
print("jelly =", jelly)
print("jelly speaks:", end=" ")
jelly.speak()

jelly.get_name() #returns nothing because its name is not set yet
jelly.set_name("JellyBelly")
print("jelly.get_name() =", jelly.get_name())
print("jelly =", jelly)
print("Animal.__str__(jelly) =", Animal.__str__(jelly))

blob = Animal(1)
print("blob =", blob)
blob.set_name()
print("blob =", blob)
print("blob speaks:", end=" ")
'''
blob.speak() # throws attribute error because there is no speak() method in Animal class
'''
print()
print("__")
print()


# Subclass Rabbit
class Rabbit(Animal):
    def speak(self):
        print("meep")
    def __str__(self):
        return "rabit:" + str(self.name) + ":" + str(self.age)    

peter = Rabbit(5)
print("peter speaks:", end=" ")
peter.speak()
print("jelly =", jelly)
print("__")
print()


# Subclass Person
class Person(Animal):
    def __init__(self, name, age):
        Animal.__init__(self, age)
        Animal.set_name(self, name)
        self.friends = []
    def get_friends(self):
        return self.friends
    def add_friends(self, fname):
        if fname not in self.friends:
            self.friends.append(fname)
    def speak(self):
        print("hello")
    def age_diff(self, other):
        # alternate way: diff = self.age - other.age
        diff = self.get_age() - other.get_age()
        if self.age > other.age:
            print(self.name, "is", diff, "years older than", other.name)
        else:
            print(self.name, "is", -diff, "years younger than", other.name)
    def __str__(self):
        return "person:" + str(self.name) + ":" + str(self.age)    
    
    
eric = Person("eric", 45)
john = Person("john", 55)
print(eric)
print(john)
print("eric speaks:", end=" ")
eric.speak()
print("eric.age_diff(john):", end=" ")
eric.age_diff(john)
print("Person.age_diff(john, eric):", end=" ")
Person.age_diff(john, eric)
print("__")
print()



# Creating a sub-subclass Student from Person, which is a subclass of class Animal
# Sub-subclass Student
class Student(Person):
    def __init__(self, name, age, major=None):
        Person.__init__(self, name, age)
        self.major = major
    def change_major(self, major):
        self.major = major
    def speak(self):
        r = random.random()
        if r < 0.25:
            print("i have homework")
        elif 0.25 <= r < 0.5:
            print("i need sleep")
        elif 0.5 <= r < 0.75:
            print("i should eat")
        else:
            print("i am watching tv")
    def __str__(self):
        return "student:" + str(self.name) + ":" + str(self.age) + ":" + str(self.major) 
        
fred = Student('Fred', 18, 'Course VI')
print(fred)    
fred.speak()
fred.speak()
fred.speak()
fred.speak()
