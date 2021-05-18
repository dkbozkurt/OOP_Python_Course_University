# -*- coding: utf-8 -*-
"""
Created on Mon May 17 16:07:25 2021

@author: Doğukan Bozkurt
"""
import CellPhone

def main():
    man= input("Enter the manufacturer: ")
    mod= input("Enter the model number: ")
    retail= int(input("Enter the retail price: "))
    
    my_phone= CellPhone.CellPhone(man,mod,retail)
    
    print("Here is the data that you entered: ")
    print("Manufacturer: ", my_phone.get_manufact())
    print("Model Number: ",my_phone.get_model())
    print("Retail Price: $", format(my_phone.get_retail_price(),',.2f'),sep='')
        
main()