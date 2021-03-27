# -*- coding: utf-8 -*-
"""
Created on Mon Mar 22 00:52:35 2021

@author: Doğukan Bozkurt
"""
#Flowchartet question

num=int(input("Enter an input value: "))
n=0
copy_num=num

while num!=0:
    num=num/10
    n+=n
print("n: ",n)

if n%2==1:
    
    i=0
    left_sum=0
    right_sum=0
    num=copy_num
    while i<n:
        rem=num%10
        num=num/10
        if i<(n/2):
            right_sum=right_sum+rem
        elif i>(n/2):
            left_sum=left_sum+rem
        else:
            i+=1
            
    if left_sum==right_sum:
        print("X number.")
    else:
        print("Not X number.")
else:
    print("Not X number.")  