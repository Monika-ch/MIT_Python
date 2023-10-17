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
        #return (self.getLastName() + " says: " + utterance)
        # or change MIT person's speak method to -
        return (self.name + " says: " + utterance)
    

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
print("p1 < p4 = throws Attribute error because there is no idNum on Person")
#print("p1 < p4 =", p1 < p4) #uncomment and test it out
print("while p4 < p1 =", p4 < p1)
print("_________________________________")
print()

# Substitution Principle
class Student(MITPerson):
    pass

class UG(Student):
    def __init__(self, name, classYear):
        MITPerson.__init__(self, name)
        self.year = classYear
        
    def getClass(self):
        return self.year
    
    def speak(self, utterance):
        return MITPerson.speak(self, "Dude, " + utterance)
    
class Grad(Student):
    pass
    
class TransferStudent(Student):
    pass

def isStudent(obj):
    return isinstance(obj, Student)

s1 = UG('Matt Damon', 2017)
s2 = UG('Ben Affleck', 2017)
s3 = UG('Lin Manuel Miranda', 2018)
s4 = Grad('Leonardo di Caprio')
s5 = TransferStudent('Robert deNiro')

print("s1 =", s1)
print("s1.getClass() =", s1.getClass())
print("s1.speak('where is the quiz?') =", s1.speak('where is the quiz?'))
print("s2.speak('I have no clue!') =", s1.speak('I have no clue!'))
print("s4 =", s4)
print("_________________________________")
print()

class Professor(MITPerson):
    def __init__(self, name, department):
        MITPerson.__init__(self, name)
        self.department = department
    def speak(self, utterance):
        newUtterance = 'In course ' + self.department + ' we say '
        return MITPerson.speak(self, newUtterance + utterance)
    def lecture(self, topic):
        return self.speak('it is obvious that ' + topic)
    
faculty = Professor('Doctor Arrogant', 'six')
print("faculty =", faculty)
print("m1.speak('hi there') =>", m1.speak('hi there'))
print("s1.speak('hi there') =>", s1.speak('hi there'))
print("faculty.speak('hi there') =>", faculty.speak('hi there'))
print("faculty.lecture('hi there') =>", faculty.lecture('hi there'))

print("__")
print()
