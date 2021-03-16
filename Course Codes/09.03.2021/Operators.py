# -*- coding: utf-8 -*-
"""
Created on Sun Mar  7 21:33:22 2021

@author: Doğukan Bozkurt
"""
"""

// : Integer division : Divides one number by another and gives the result as an integer
** : Exponent : Raises a number to a power

"""
print(5/2)
print(5//2)

#Uses floor func. with negative numbers.
print(-5//2)
print(-6//5)

#Total seconds to -> hours,minutes,seconds
total_seconds=float(input("Enter a number of seconds: "))
hours = total_seconds//3600
minutes=(total_seconds/60)%60
seconds=total_seconds%60
print("Here is the time in hours, minutes and seconds:")
print("Hours: ",hours)
print("Minutes: ",minutes)
print("Seconds: ",seconds)

"""
Print func-
    \ ( in print func.): bir alt satira print icerigini yazmamiza yardim eder.
    \n, \t, \', \", \\
"""

rnumber=5000.0/12
print(rnumber)
#The number only contains x digits after . -> '.xf'
print(format(rnumber,".2f"))
#The number start to write the value from respect to right. after openin 20spaces.
print(format(123456,"20d"))