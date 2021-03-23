# -*- coding: utf-8 -*-
"""
Created on Fri Feb 15 15:41:41 2019

@author: burak
"""

r=int(input('Enter r '))
g=int(input('Enter g '))
b=int(input('Enter b '))

w=max(r/255,g/255,b/255)

c=(w-r/255)/w
m=(w-g/255)/w
y=(w-b/255)/w
k=1-w

print("c=",format(c,".2f"))
print("m=",format(m,".2f"))
print("y=",format(y,".2f"))
print("k=",format(k,".2f"))