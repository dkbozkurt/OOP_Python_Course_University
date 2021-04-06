# -*- coding: utf-8 -*-
"""
Created on Tue Apr  6 00:52:49 2021

@author: Doğukan Bozkurt
"""
#Telephone number 555-GET-FOOD

telephone_dict={
    'A':2,
    'B':2,
    'C':2,
    'D':3,
    'E':3,
    'F':3,
    'G':4,
    'H':4,
    'I':4,
    'J':5,    
    'k':5,    
    'L':5,
    'M':6,    
    'N':6,    
    'O':6,
    'P':7,    
    'Q':7,    
    'R':7,    
    'S':7,    
    'T':8,
    'U':8,
    'V':8,
    'W':9,
    'X':9,
    'Y':9,
    'Z':9
        }

def converterFunc(nums,t_d):
    n=""
    for i in range(0,4):
        n+=nums[i]
        
    for i in range(4,12):
        for key,value in t_d.items():
            if i==7:
                n+="-"
                break
            if nums[i] in key:
                n+=str(value)
            
    return n
    
def main():
    t_numbers=input("Please enter a 10-character telephone number in the format:\nXXX-XXX-XXXX\n")
    print(str(converterFunc(t_numbers,telephone_dict)))
    
main()
