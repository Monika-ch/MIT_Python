#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Oct 13 19:26:14 2023

@author: monika
"""

# Class Variables: with an example of class Animal and subclass Rabbit

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


# Creating subclass Rabbit from parent class Animal

# Subclass Rabbit
class Rabbit(Animal):
    tag = 1
    def __init__(self, age, parent1 = None, parent2 = None):
        Animal.__init__(self, age)
        self.parent1 = parent1
        self.parent2 = parent2
        self.rid = Rabbit.tag
        # tag is used to give unique id to each new rabbit instance
        Rabbit.tag += 1
    def get_rid(self):
        # zfill: is a method on a string to pad the beginning with zeros
        # for example, 001 not 1
        return str(self.rid).zfill(3)
    def get_parent1(self):
        return self.parent1   
    def get_parent2(self):
        return self.parent2
    def __add__(self, other):
        # returning object of same type as this class
        return Rabbit(0,self,other)
        # recall Rabbit's __init__(self, age, parent1 = None, parent2 = None)
    def __eq__(self, other):
        # determine if the two Rabbit instances have same parents
        parents_same = self.parent1.rid == other.parent1.rid \
                       and self.parent2.rid == other.parent2.rid
        parents_opposite = self.parent1.rid == other.parent2.rid \
                       and self.parent2.rid == other.parent1.rid                     
        return parents_same or parents_opposite
    
peter = Rabbit(2)
peter.set_name('Peter')
hopsy = Rabbit(3)
hopsy.set_name('Hopsy')

cotton = Rabbit(1, peter, hopsy)
cotton.set_name('Cottontail')
print("cotton =", cotton)
print("cotton.get_parent1() =", cotton.get_parent1())

mopsy = peter + hopsy
mopsy.set_name("Mopsy")
print(mopsy.get_parent1())
print(mopsy.get_parent2())


print("__")
print("Does Mopsy and Hopsy have same parents?", "\n", "    mopsy == cotton:", mopsy == cotton)
