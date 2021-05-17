# -*- coding: utf-8 -*-
"""
Created on Tue Apr  6 10:23:24 2021

@author: Doğukan Bozkurt
"""
#DICTIONARIES
#Each item has a key and a value.
#Keys can not be dublicated, immutable but values can be any type!!!
"""
phonebook={} # Empty dict
phonebook={"Chris":"555-1111","Katie":"555-2222","Joanne":"555-3333"}
print(phonebook)
print(phonebook["Katie"])

# The items in a dict arent stored in any order.so you can not use a numberic index.
# Instead, you use a key to get a value!!!

if 'Chris' in phonebook:
    print("Chris' phone number is ",phonebook["Chris"])

#Dictionaries are mutable objects
#If key already exist, 
phonebook["Dogukan"]='555-6666'
print(phonebook)

#Deleting Elements

del phonebook["Dogukan"]
print(phonebook)

#Lenght
print(len(phonebook))
"""

#Mixing Data Types in a Dict
"""
test_scores={"Kayla":[88,92,100],
             "Luis":[95,74,81],
             "Sophie":[72,88,91],
             "Ethan": [70,75,78]}
print(test_scores)
print(test_scores["Sophie"])
"""

#Using for loop to iterate over a dict.
"""
test_scores={"Kayla":[88,92,100],
             "Luis":[95,74,81],
             "Sophie":[72,88,91],
             "Ethan": [70,75,78]}
for key in test_scores:
    print(key,test_scores[key])
"""   
 
#Dict Methods : clear(), get(), items(), keys(), pop(), popitem(), values()
"""
#get()
print(test_scores.get("Kayla","Not found"))
print(test_scores.get("Ayse","Not found"))

#items()
for k,v in test_scores.items():
    print(k,v)

#values()
print(test_scores.values())
"""

#Stroing names and birthdays in a dict
"""
LOOK_UP=1
ADD =2
CHANGE=3
DELETE=4
QUIT=5

def main():
    birthdays={}
    choice=0
    
    while choice != QUIT:
        choice = get_menu_choice()
        
        if choice==LOOK_UP:
            look_up(birthdays)
        elif choice ==ADD:
            add(birthdays)
        elif choice ==CHANGE:
            change(birthdays)
        elif choice ==DELETE:
            delete(birthdays)
            
def get_menu_choice():
    print()
    print("Friends and Their Birthdays")
    print("---------------------------")
    print("1. Look up a birthday")
    print("2. Add a new birthday")
    print("3. Change a birthday")
    print("4. Delete a birthday")
    print("5. Quit the program")
    print()
    
    choice=int(input("Enter your choice: "))
    
    return choice

def look_up(birthdays):
    
    name=input("Enter a name: ")
    print(birthdays.get(name,"Not found."))
      
def add(birthdays):
    name=input("Enter a name: ")
    bday=input("Enter a birthday: ")
    if name not in birthdays:
        birthdays[name]=bday
    else:          
        print("That entry already exists.")
    
def change(birthdays):
    name=input("Enter a name: ")
    
    if name in birthdays:
        bday= input("Enter the new birthday: ")
        birthdays[name] = bday
    else:
        print("That name is not found")
        
def delete(birthdays):
    name=input("Enter a name: ")
    
    if name in birthdays:
        del birthdays[name]
    else:
        print("That name is not found.")
main()
"""