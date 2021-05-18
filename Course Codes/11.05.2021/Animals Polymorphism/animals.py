# -*- coding: utf-8 -*-
"""
Created on Mon May 17 16:54:27 2021

@author: Doğukan Bozkurt
"""
# Mammal Superclass

class Mammal:
    
    def __init__(self,species):
        self.__species=species
        
    def show_species(self):
        print("I am a ",self.__species)
        
    def make_sound(self):
        print("Grrrrr")
 
        
# Dog Subclass

class Dog(Mammal):
    def __init__(self):
        
        Mammal.__init__(self,'Dog')
        
    def make_sound(self):
        print('Woof! Woof!')
        

# Cat Subclass

class Cat(Mammal):
    def __init__(self):
        
        Mammal.__init__(self,'Cat')
        
    def make_sound(self):
        print('Meow')
        