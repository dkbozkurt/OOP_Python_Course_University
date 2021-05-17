# -*- coding: utf-8 -*-
"""
Created on Tue Apr  6 11:33:56 2021

@author: Doğukan Bozkurt
"""
#SETS

"""
myset=set() #Creating an empty set
myset=set(["a","b","c"]) # Creating a set with initial values

"""
#Sets cannot contain duplicate arguments !!!
"""
myset=set("one two three")
print(myset)
"""

#Adding and Removing Elements
#.add(), update(), remove(), discard()
"""
myset=set()
myset.add(1)
myset.add(2)
myset.add(3)
print(myset)
myset.add(2)
print(myset)

myset.update([4,5,6])
print(myset)

myset.remove(1) #writes a KeyError exception
myset.discard(5)
print(myset)
"""

#Finding the Union,Intersection and Difference of Sets
"""
set1=set([1,2,3,4])
set2=set([3,4,5,6])
set3=set1.union(set2)
print(set3)
#Second way
set3=set1 | set2
print(set3)

set4=set1.intersection(set2)
print(set4)
#Second way
set4=set1 & set2
print(set4)

set5=set1.difference(set2)
print(set5)
#Second way
set5=set1 - set2
print(set5)

set6=set1.symmetric_difference(set2)
print(set6)
#Second way
set6=set1 ^ set2
print(set6)
"""

#Subsets and Supersets of Sets
"""
set1=set([1,2,3,4])
set2=set([2,3])
print(set2.issubset(set1))
print(set1.issuperset(set2))

print(set2 <= set1)
print(set1 >= set2)
print(set1 <= set2)
"""