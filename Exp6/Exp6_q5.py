# -*- coding: utf-8 -*-
"""
Created on Sun Apr  4 17:33:42 2021

@author: Doğukan Bozkurt
"""

import math
import numpy as np

def sigmoidFunc(x):
    sigmoided=np.array([])
    for element in x:
        element = 1/(1+math.exp(-element))
        sigmoided = np.append(sigmoided, element)
        
    return sigmoided

def weights(iL,hL,oL):
    w1 = generateImage(hL,iL)   #48x32
    w2 = generateImage(oL,hL)   #3x48
    return w1,w2
  
def biases(hL,oL):
    b1= generateImage(hL,1) #48x1
    b2= generateImage(1,oL) #1x3
    return b1, b2
    
def twoLayerNetwork(x,b1hL,b2oL,w1,w2):
    h1= sigmoidFunc(np.add(np.matmul(w1,x), b1hL).flatten())    #1x48
    
    """
    print("h1:",h1)
    print("w2.shape",w2.shape)
    print("matmul",np.matmul(w2,h1))
    print("np.add",np.add(np.matmul(w2,h1),b2oL))
    """
    score= np.add(np.matmul(w2,h1),b2oL)    #3x1
    return score #3x1


def generateImage(rows, columns):
    
    image = np.random.rand(rows, columns)   
    return image

def check(score):
    
    print ("Score:",score)
    max_index= np.argmax(score)
    dict_res={0:'Image\'s class is Cat',1:'Image\'s class is Dog!',2:'Image\'s class is Bird!'}
    print(dict_res[max_index])
        
def main():
    
    row=1024; column=1
    hiddenLayer=48; outputLayer=3
    
    tensor = generateImage(row,column)  #InputLayer
    w_1,w_2 = weights(row, hiddenLayer , outputLayer)
    b_1, b_2 = biases(hiddenLayer, outputLayer)    
    score = twoLayerNetwork(tensor, b_1, b_2, w_1, w_2)
    
    check(score)
    
main()