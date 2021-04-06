# -*- coding: utf-8 -*-
"""
Created on Sun Apr  4 21:19:58 2021

@author: Doğukan Bozkurt
"""

import numpy as np

def generateData(limit):
    data=np.random.randint(1,4,limit)
    print("Data:\n", data)
    return data    
    
def indicesCheck(data,begin,end,label):
    tp=0; fn=0; fp=0  
    index=0
    for i in data:
        
        if index in range(begin,end):
            if i==label:
                tp+=1
            else:
                fn+=1
        elif i == label:
            fp+=1        
        
        index+=1
        
    calculations(tp,fp,fn,label)
        
def calculations(tp,fp,fn,label):
    precision=tp/(tp+fp)
    recall=tp/(tp+fn)
    f1=2*((precision*recall)/(precision+recall))
    printMenu(precision,recall,f1,label)
    
def printMenu(pre,rc,f1,label):
    print("\nFor Class {0}:\n   Precision: {1}\n   Recall: {2}\n   F1: {3}\n".format(label,pre,rc,f1))
 
def main():
    
    dict_label={"Class_1" :1,"Class_2":2,"Class_3":3}
    data=generateData(100)
    
    indicesCheck(data,0,40,dict_label["Class_1"])
    indicesCheck(data,40,90,dict_label["Class_2"])
    indicesCheck(data,90,100,dict_label["Class_3"])
    
main()