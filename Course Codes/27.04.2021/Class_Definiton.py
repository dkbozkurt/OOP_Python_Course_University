# -*- coding: utf-8 -*-
"""
Created on Tue Apr 27 10:58:32 2021

@author: Doğukan Bozkurt
"""
import random

class Coin:
    def __init__(self):
        self.sideup="Heads"
        
    def toss(self):
        if random.randint(0,1)==0:
            self.sideup="Heads"
        else:
            self.sideup="Tails"
            
    def get_sideup(self):
        return self.sideup
    
def main():
    
    my_coin=Coin()
    
    print("At the beginning, side up is: ", my_coin.get_sideup())
    
    my_coin.toss()     
    print("After flipping the coin, side up is: ", my_coin.get_sideup())
    
main()