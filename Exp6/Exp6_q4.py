# -*- coding: utf-8 -*-
"""
Created on Tue Apr  6 09:56:00 2021

@author: Doğukan Bozkurt
"""
import random

#random.sample(range(1,100),3) #creates 3 unique numbers in range. 

def generate(rng):
    numbers=[]
    for i in range(rng):
        numbers.append(random.randint(1,10))
        
    print("Numbers:\n",numbers)
    dictionaryCheck(numbers,rng)
    
def dictionaryCheck(nums,rng):
    dict_sample={ 1:0,2:0,3:0,4:0,5:0,6:0,7:0,8:0,9:0,10:0}
    
    for i in range(0,rng):
        if nums[i] in dict_sample.keys():
            dict_sample[nums[i]]+=1
    print(dict_sample)
    
def main():
    generate(100)
    
main()