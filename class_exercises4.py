#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Oct 13 18:41:55 2023

@author: monika
"""

# Class Exercise
# Python supports a limited form of multiple inheritance, demonstrated in the following code:

class A(object):
    def __init__(self):
        self.a = 1
    def x(self):
        print("A.x")
    def y(self):
        print("A.y")
    def z(self):
        print("A.z")

class B(A):
    def __init__(self):
        A.__init__(self)
        self.a = 2
        self.b = 3
    def y(self):
        print("B.y")
    def z(self):
        print("B.z")

class C(object):
    def __init__(self):
        self.a = 4
        self.c = 5
    def y(self):
        print("C.y")
    def z(self):
        print("C.z")

class D(C, B):
    def __init__(self):
        C.__init__(self)
        B.__init__(self)
        self.d = 6
    def z(self):
        print("D.z")
        
        
"""Which __init__ methods are invoked and in which order is determined by the 
coding of the individual __init__ methods.

When resolving a reference to an attribute of an object that's an instance of 
class D, Python first searches the object's instance variables then uses a 
simple left-to-right, depth first search through the class hierarchy. 
In this case that would mean searching the class C, followed the class B and 
its superclasses (ie, class A, and then any superclasses it may have, et cetera).

With the definitions above if we define: obj = D()
then what is printed by each of the following statements?"""

obj = D()

print(obj.a)
print(obj.b)
print(obj.c)
print(obj.d)
obj.x()
obj.y()
obj.z()


## In the above code why obj.y() prints "C.y" and not "B.y"???
## And why it follows a different rule for print(obj.a) and prints 2 instead of 4???

"""
The reason why obj.y() prints “C.y” and not “B.y” is because of the 
method resolution order (MRO) in Python inheritance. 

The MRO determines the order in which the base classes are searched when 
looking for a method or an attribute. In Python, the MRO follows the C3 
linearization algorithm, which ensures that the subclasses precede their base 
classes and that the order is consistent and monotonic.

In the code, class D is defined as a subclass of C and B, which are both
subclasses of A and object. The MRO of class D is:

D -> C -> B -> A -> object

This means that when you call obj.y(), Python will first look for the method y 
in class D. If it does not find it, it will look in class C, then in class B, 
then in class A, and finally in object. In this case, it finds the method y 
in class C, so it executes it and prints “C.y”.

However, when you print obj.a, Python will look for the attribute a in class D 
first. If it does not find it, it will look in class C, then in class B, and 
so on. In this case, it finds the attribute a in both class C and class B, 
but it will use the one that is assigned later in the code. Since you have 
called C.init(self) before B.init(self) in the constructor of class D, the 
attribute a from class B will overwrite the one from class C. Therefore, 
obj.a will have the value 2 instead of 4.
"""