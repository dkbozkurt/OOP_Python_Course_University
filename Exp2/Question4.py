# -*- coding: utf-8 -*-
"""
Created on Sun Mar  7 20:00:37 2021

@author: Doğukan Bozkurt
"""
#RGB to CMYK
print("RGB to CMYK converter")
r=int(input("Level of Red: "))
g=int(input("Level of Green: "))
b=int(input("Level of Blue: "))

w= max(r/255,g/255,b/255)
c= (w-r/255)/w
m= (w-g/255)/w
y=(w-b/255)/w
k=1-w

print("\nCyan Color: ",round(c,5),"\nMagenta Color: ",m,"\nYellow Color: ",y,"\nBlack Color: ",round(k,5))

#Try to use .format() in print funcs.