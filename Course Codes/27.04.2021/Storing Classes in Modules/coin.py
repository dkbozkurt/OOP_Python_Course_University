# -*- coding: utf-8 -*-
"""
Created on Tue Apr 27 11:11:37 2021

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
    