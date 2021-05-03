# -*- coding: utf-8 -*-
"""
Created on Tue Apr 27 11:16:06 2021

@author: Doğukan Bozkurt
"""

class BankAccount:
    
    def __init__(self,bal):
        self.__balance=bal
    
    def deposit(self,amount):
        self.__balance+=amount
        
    def withdraw(self,amount):
        if self.__balance>=amount:
            self.__balance-=amount
            
        else:
            print("Error : Insufficient fuds")
    
    def get_balance(self):
        return self.__balance
    
    def __str__(self):
        return "The balance is " + format(self.__balance,".2f")
            