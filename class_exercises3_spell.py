#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Oct 13 18:20:13 2023

@author: monika
"""

# Class Exercise: Spell

# Consider the following code:

class Spell(object):
    def __init__(self, incantation, name):
        self.name = name
        self.incantation = incantation

    def __str__(self):
        return self.name + ' ' + self.incantation + '\n' + self.getDescription()
              
    def getDescription(self):
        return 'No description'
    
    def execute(self):
        print(self.incantation)


class Accio(Spell):
    def __init__(self):
        Spell.__init__(self, 'Accio', 'Summoning Charm')
    """   
    def getDescription(self):
        return 'This charm summons an object to the caster, potentially over a significant distance.'
    """

class Confundo(Spell):
    def __init__(self):
        Spell.__init__(self, 'Confundo', 'Confundus Charm')

    def getDescription(self):
        return 'Causes the victim to become confused and befuddled.'

def studySpell(spell):
    print(spell)

spell = Accio()
spell.execute() # Accio
studySpell(spell) #Summoning Charm Accio #No description
studySpell(Confundo()) # Confundus Charm Confundo #Causes the victim to become confused and befuddled.