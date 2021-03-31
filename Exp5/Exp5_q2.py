# -*- coding: utf-8 -*-
"""
Created on Mon Mar 29 11:53:03 2021

@author: Doğukan Bozkurt
"""
#Footbal League

import random

def generate():
    win=random.randint(15, 25)
    draw=random.randint(3, 5)
    lost=30-(win+draw)
    return win,draw,lost
    
#Calculates the total score of each team

def points(x):
    total=x[0]*3+x[1]
    return total

def printTable(a,b,c,at,bt,ct):
    #If you use "{A:010}...".format(A=x) in print. It will print 10 times zero before x.
    #{:>x} works as setw() in cpp, prints x times spaces and write the following indexed format parameters.
    print("{}{:>5}{:>6}{:>6}{:>8}".format("Team", "Won","Draw","Lost","Points"))    
    print(" A{:>7}{:>6}{:>6}{:>8}".format(a[0],a[1],a[2],at)) 
    print(" B{:>7}{:>6}{:>6}{:>8}".format(b[0],b[1],b[2],bt)) 
    print(" C{:>7}{:>6}{:>6}{:>8}".format(c[0],c[1],c[2],ct)) 
    
def main():
    
    a=generate(); b=generate(); c=generate()
    atotal=points(a); btotal=points(b); ctotal=points(c)
    printTable(a,b,c,atotal,btotal,ctotal)
    
    if atotal>btotal and atotal>ctotal: 
        print("\nThe winner team is A!") 
    elif btotal>atotal and btotal>ctotal: 
        print("\nThe winner team is B!") 
    elif ctotal>atotal and ctotal>btotal: 
        print("\nThe winner team is C!")
    else:
        print("There is no champion in the season!")
    
        
main()