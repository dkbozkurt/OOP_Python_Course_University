# -*- coding: utf-8 -*-
"""
Created on Mon Apr  5 17:36:51 2021

@author: Doğukan Bozkurt
"""
#The Lo Shu Magic Square

import numpy as np

numbers=[1,2,3,4,5,6,7,8,9]

def isLoShuMagicSquare(square,rows,cols):
    a=0;b=0
    for i in range(0,rows):
        
        #np.sum(array) returns sum of all the elements in array.   
        if np.sum(square[i][:])==15 and np.sum(square[:][i])==15:
            a+=np.sum(square[i][i])
            b+=np.sum(square[i][(rows-1)-i])
            i+=1
            
            if a==15 and b==15:
                print("The square matrix is a Lo Shu Magic Square!")
                
        else:
            print("The square matrix is not a Lo Shu Magic Square!")
            break
       
def generateGrid(rows,cols):    
    
    #creating an array by sizes rows,cols in range 1 to 9
    #grid=np.random.randint(1,9,(rows,cols))
    
    #By using replace=False; we choose only one value, one time from the list.
    #Or random.sample(range(1,100),3) creates 3 unique numbers in range too !!!
    grid=np.random.choice(numbers,9,replace=False)
    
    #Check for correct numbers
    #grid=np.array([4,9,2,3,5,7,8,1,6])
    
    #Covnerting the 1d list into expected matrix
    grid=grid.reshape((rows,cols))
    
    print("Matrix:\n",grid)
    
    return grid
    
def main():
    
    isLoShuMagicSquare(generateGrid(3,3),3,3)

main()    