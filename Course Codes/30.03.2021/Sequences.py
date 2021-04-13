# -*- coding: utf-8 -*-
"""
Created on Tue Mar 30 09:08:01 2021

@author: Doğukan Bozkurt
"""
#Sequences
"""
LISTS (Vector in C++)0

Lists are mutable,which means that a program can change its contents.

We can use repetition operator with lists.

Python uses 0 index as the starting index

If you omit end index Python uses the length of list as the end index.

If you omit both stating and end indives, Python gets a copy of the entire list.

"""
"""
TUPLES

Tuples are immutable its contents cannot be changed.
"""
#dk_list=[] Empty list !!!
#info=["Dogukan",35,3.55]
#number=list(range(0,5))
#numbers=[1,2,3]*3

even_numbers=list(range(0,10,2))
print(even_numbers)

list1=[1,2,3,4]
list2=[5,6,7,8]
list1+=list2
print(list1)

days=["Monday","Tuesday","Wednesday","Thursday","Friday","Saturday","Sunday"]
print(days[1:3])
print(days[1:7:2])
print(days[2:])
print(days[:5])
print(days[:])


del list1[5]
print(max(list1))
print(min(list1))

#Copying a list into another one
list3=list1.copy()
#or
#list3=list1[:]
print(list3)

#Two Dimensional Lists
list4=[list1,list2,list3]
print(list4)
print(list4[0])
print(list4[0][0])

#TUPLES

tuple1=(1,2,3,4,5)
#Tuples are not containing "append, remove, insert, reverse, sort...

list5=list(tuple1)
tuple2=tuple(list5)