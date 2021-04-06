# -*- coding: utf-8 -*-
"""
Created on Sun Apr  4 13:29:41 2021

@author: Doğukan Bozkurt
"""
import random
import numpy as np

#Using ascii is an option while using random keys
#import string
#string.ascii_letters

def correctOrWrong(sa,ca,qn):
    corrects=0
    inc_std_ans=[]
    for q in range(qn):
        if ca[q]==sa[q]:
            corrects+=1
        else:
            inc_std_ans.append(q+1)
    printMenu(corrects,inc_std_ans,qn)

def printMenu(corrects,isa,qn):
    
    if corrects>=15:
        print("Student Passed!")
    else:
        print("Student Failed!")
        
    print("\n\tTotal number of correct answers: {0}\n\tTotal number of incorrect answers: {1}".format(corrects,qn-corrects))
    print("\nQuestion numbers of the incorrectly answered:\n",isa[:])
    
def generateRandomAnswer(_list,qn):
    #Chooses random element from the list
    answers=random.choices(_list,k=qn) # where k is the number of answers
    return answers
    
def main():
    question_num=20
    correct_answers=['A','C','A','A','D','B','C','A','C','B','A','D','C','A','D','C','B','B','D','A']
    possible_answers='ABCD'
    student_answers=generateRandomAnswer(possible_answers,question_num)
    correctOrWrong(student_answers, correct_answers,question_num)
    
main()
