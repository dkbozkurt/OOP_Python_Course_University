# -*- coding: utf-8 -*-
"""
Created on Sun Mar  7 00:34:49 2021

@author: Doğukan Bozkurt
"""

print("Python Programming course will be funny.")
print("Python Programming course\nwill be funny.")
#Way1
print("Python","Programming","course","will","be","fuuny.",sep='\n')
#Way2
text = "Python Programming course\nwill be funny.".split(' ')
print(*text,sep='\n')
#Way3
print("\n".join(text))