# -*- coding: utf-8 -*-
"""
Created on Tue Apr 27 11:18:30 2021

@author: Doğukan Bozkurt
"""
import BankAccount


def main():
    
    # Create a BankAccount object
    savings=BankAccount.BankAccount(3000)
    
    savings.deposit(2000)
    
    #print("Balance is ", savings.get_balance())
    print(savings)
    
    savings.withdraw(4000)
    
    #print("New balance is ", savings.get_balance())
    print(savings)
    
main()