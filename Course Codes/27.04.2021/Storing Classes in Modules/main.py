# -*- coding: utf-8 -*-
"""
Created on Tue Apr 27 11:13:51 2021

@author: Doğukan Bozkurt
"""
import coin

def main():
    
    # coin. must added when calling the class' object.
    my_coin=coin.Coin()
    
    print("At the beginning, side up is: ", my_coin.get_sideup())
    
    my_coin.toss()     
    print("After flipping the coin, side up is: ", my_coin.get_sideup())
    
main()