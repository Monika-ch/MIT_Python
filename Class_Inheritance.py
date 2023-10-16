#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Oct 15 20:53:26 2023

@author: monika
"""

# Building a class and using Inheritance

import datetime

class Person(object):
    def __init__(self, name):
        """create a person called name"""
        self.name =  name
        self.birthday = None
        self.lastname = name.split(" ")[-1]
        
    def getLastName(self):
        """return self's last name"""
        return self.lastname
    
    def setBirthday(self, month, day, year):
        """return self's birthday to birthDate"""
        self.birthday = datetime.date(year, month, day)
    
    def getAge(self):
        """return self's current age in days"""
        if self.birthday == None:
            raise ValueError
        return (datetime.date.today() - self.birthday).days
    
    def __lt__(self, other):
        """returns True if self's name is lexicographically less than
        other's name, and False otherwise"""
        if self.lastname == other.lastname:
            return self.name < other.name
        return self.lastname < other.lastname
    
    def __str__(self):
        """return self's name"""
        return self.name
    
    
p1 = Person('Mark Zuckerberg')
p1.setBirthday(5, 14, 84)
p2 = Person('Drew Houston')
p2.setBirthday(3, 4, 83)
p3 = Person('Bill Gates')
p3.setBirthday(10, 28, 55)
p4 = Person('Andrew Gates')
p5 = Person('Steve Wozniak')

personList = [p1, p2, p3, p4, p5]

print("p1 =", p1)
print("__")
print()

print("* PersonList:")
for e in personList:
    print(e)
print("__")
print()

print("* Sorted PersonList:")
personList.sort()
for e in personList:
    print(e)
print("_________________________________")
print()


class MITPerson(Person):
    nextIdNum = 0 #next ID number to assign
    
    def __init__(self, name):
        Person.__init__(self, name) #initialize Person attributes
        self.idNum = MITPerson.nextIdNum #MITPerson attribute: unique ID
        MITPerson.nextIdNum +=1
        
    def getIdNum(self):
        return self.idNum
    
    # sorting MIT people uses their ID number, not name!
    def __lt__(self, other):
        return self.idNum < other.idNum
    
    def speak(self, utterance):
        return (self.getLastName() + " says: " + utterance)
    

m3 = MITPerson('Mark Zuckerberg')
Person.setBirthday(m3, 5, 14, 84)
m2 = MITPerson('Drew Houston')
Person.setBirthday(m2, 3, 4, 83)
m1 = MITPerson('Bill Gates')
Person.setBirthday(m1, 10, 28, 55)

print("m1 =", m1)
print("m3 =", m3)
print(m1.speak('hi there!'))
print("__")
print()


MITPersonList = [m1, m2, m3]


print("** MITPersonList:")
for e in MITPersonList:
    print(e)
print("__")
print()

print("** Sorted MITPersonList:")
MITPersonList.sort()
for e in MITPersonList:
    print(e)
print("_________________________________")
print()


# Example Using Hierarchy
p1 = MITPerson('Eric') #idNum will 0 from MITPerson subclass from Person
p2 = MITPerson('John') #idNum will 1
p3 = MITPerson('John') #idNum will 2
p4 = Person('John') # NO idNum on Person class
print("p1 < p2 =", p1 < p2)
#print("p1 < p4 =", p1 < p4) #uncomment and test it out
print("p4 < p1 =", p4 < p1)
print("__")
print()