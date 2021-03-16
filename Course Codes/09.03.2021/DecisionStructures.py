# -*- coding: utf-8 -*-
"""
Created on Tue Mar  9 10:20:22 2021

@author: Doğukan Bozkurt
"""
#Decision Structures

A_Score=90
B_Score=80
C_Score=70
D_Score=60
F_Score=50


score=int(input("Enter your score:"))

if score >=A_Score:
    print("You got A!")
elif score>=B_Score:
    print("You got B!")
elif score>=C_Score:
    print("You got C!")   
elif score>=D_Score:
    print("You got D!")   
elif score>=F_Score:
    print("You failed!")
elif score>100 or score<0:5
    print("You entered a wrong value!")
    
"""
and           && 
or            \\
not           !=
"""