# -*- coding: utf-8 -*-
"""
Created on Mon Mar 29 14:40:16 2021

@author: Doğukan Bozkurt
"""

def get_name():
    first = input("Enter your first name: ")
    last = input("Enter your last name: ")
    
    return first, last

first_name,last_name=get_name()

print("Name: {0}\nLastName: {1}".format(first_name,last_name))