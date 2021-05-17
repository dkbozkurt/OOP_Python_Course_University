# -*- coding: utf-8 -*-
"""
Created on Tue Apr  6 09:10:37 2021

@author: Doğukan Bozkurt
"""


#Accesing the individual characters in a string
"""
def main():
    c=0
    
    my_str=input("Enter a sentence: ")
    
    for ch in my_str:
        if ch== 'T' or ch=='t':
            c+=1
    print('the letter T appears',c,"times.")
    
main()
"""

#Indexing
"""
my_string="Roses are red"
print(my_string[0],my_string[6],my_string[10])
print(my_string[-1],my_string[-2],my_string[-13])
"""

# String Concatentaion
"""
message='Hello '+'world'
print(message)
message+=' yani sa'
print(message)
"""
#string are immutable which means that once they are created, they can not be changed.
#You can not use name[0]='K'

#String Slicing
"""
full_name="Parry Lynn Smith"
my_string=full_name[:]

print(my_string)
print(full_name[6:16:2])
"""

#in and not in
"""
names= "Bill Joanne Susan Chris Juan Katie"

if'Pierre' in names:
    print("1-True")
else:
    print("1-False")

if'Pierre' not in names:
    print("2-True")
else:
    print("2-False")
"""

#STRING METHODS
#Bool methods : isalnum(),isalpha(),isdigit(),islower(),isspace(),isupper();
"""
string1= '123'

if string1.isdigit():
    print("y")
else:
    print("n")
"""
#Modification Methods : lower(), lstrip(), lstrip(char), rstrip(), rstrip(char), strip(), strip(char), upper();

#Other bool Methods : endswith(substring), find(substring), replace(old, new), startswith(substring)
"""
file_name="DogukanKaanBozkurt.txt"
print(file_name.endswith(".txt"))
print(file_name.find("Kaan")) # The first index

new_string=file_name.replace("Kaan","_")
print(new_string)
"""

#Spliting a string
#Python uses " " as a default split seperator. But we can specify different sep.
"""
my_string="One two thee four"
world_list=my_string.split()
print(world_list)

data_str="04/06/2021"
data_list=data_str.split('/')
print("Month:",data_list[0],"\nDay:",data_list[1],"\nYear:",data_list[2])
"""