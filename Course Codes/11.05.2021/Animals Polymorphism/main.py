# -*- coding: utf-8 -*-
"""
Created on Mon May 17 16:53:55 2021

@author: Doğukan Bozkurt
"""
import animals

# This program demonstrates polymorphism.

def main():
    
    mammal = animals.Mammal('regular animal')
    dog = animals.Dog()
    cat = animals.Cat()
    
    # Display information about each other.
    print('Here are some animals and')
    print('the sounds they make.')
    print('-------------------------')
    show_mammal_info(mammal)
    print()
    show_mammal_info(dog)
    print()
    show_mammal_info(cat)
    print()
    show_mammal_info("I am string")
    
    """
    The sow_mammal_info func accepts an object
    as an argument, and calls its show_species
    and make_sound methods.
    """
    
def show_mammal_info(creature):
    """
    isinstance : We can use the isinstance function
    to determine whether an obhect is an instance of
    a specific class, or a subclass of that class.
    """
    
    if isinstance(creature,animals.Mammal):        
        creature.show_species()
        creature.make_sound()
    else:
        print("That is not a Mammal!")
main()