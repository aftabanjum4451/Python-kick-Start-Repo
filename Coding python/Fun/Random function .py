# -*- coding: utf-8 -*-
"""
Created on Tue Jun  2 13:46:51 2020

@author: aftab
"""

import random
import numpy as np 
import math

random.random() # give rnadom float number between 0 and 1

float(random.randrange(1,10,2)) # give random int number between the provide range(1,8) 


for i in range(10):
    print(random.choice('abcdfeghd'))# give random number or letter or any thing that pass a parameter in the choice function
    
random.sample('123456789',3)# return array or list of random sequence element acording to the size of k value 

for i in range(500):
    print(random.uniform(1,2))

for i in range(5):
    print(random.sample('123456789',2))
    

    
    
    
    
    
    