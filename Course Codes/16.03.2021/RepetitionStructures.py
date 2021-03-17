# -*- coding: utf-8 -*-
"""
Created on Tue Mar 16 08:52:45 2021

@author: Doğukan Bozkurt
"""

#WHILE

#An exaple of flowchart
"""
keep_going='y'

while keep_going=='y':
    sales= float(input("Enter the amount of sales: "))
    comm_rate=float(input("Enter the commision rate: "))
    commision = sales * comm_rate
    
    print("The commision is $",format(commision, '.2f'), sep='')
    
    keep_going = input("Do you want to calculate another "+"commision (Enter y for yes): ")
 """   
#FOR

#Example 1
"""
print("I will display the odd numbers 1 through 9.")
for num in [1, 3, 5, 7, 9]:    #We can use with strings too.
    print(num)
    
#Using the Control Variable Inside the Loop

print("Number\tSquare")
print("--------------")

for number in range(1,11):
    square = number**2
    print(number,"\t",square)
"""
#An Example
"""
START_SPEED=60
END_SPEED=131
INCREMENT =10
CONVERSION_FACTOR=0.6214

print("KPH \tMPH")
print("---------------")

for kph in range(START_SPEED,END_SPEED,INCREMENT):
    mph=kph* CONVERSION_FACTOR
    print(kph,"\t",format(mph,".1f"))
"""
#Another Example
"""
print("This program displays a list of numbers")
print("and their squares")
start=int(input("Enter the starting number: "))

end=int(input("Enter the ending point: "))

print()
print("Number\tSquare")
print("--------------")

for number in range(start,end+1):
    square=number**2
    print(number, "\t", square)
"""
#An Example calculates retail prices
"""
MARK_up=2.5
another='y'

while another=='y' or another == 'Y':
    wholesale = float(input("Enter the item's " + "wholesale cost: "))
                            
    while wholesale<0:
        print("ERROR: the cost cannot be negative.")
        wholesale = float(input("Enter the item's " + "wholesale cost: "))
     
    retail = wholesale * MARK_up
    print("Retail price: $",format(retail, '.2f'), sep='')                            
    
    another=input("Do you have another item?" + "(Enter y for yes): ")
"""   
#Reverse a number

num=int(input("Enter a number: "))
rvs=0

while num!=0:
    remainder=num%10
    rvs=rvs*10+remainder
    num=num//10
    
print("Reverse of the num is: ",rvs)
