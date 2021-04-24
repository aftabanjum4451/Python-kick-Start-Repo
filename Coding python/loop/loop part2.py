# -*- coding: utf-8 -*-
"""
Created on Mon Aug 17 08:57:45 2020

@author: aftab
"""
import numpy as np

#Q Write a while loop that is initialized at 0 and stops at 15. If the counter is an even number, append the counter to a list called eve_nums.


numer=0
eve_nums=[]
while numer<=15:
     print(numer)
     if numer%2==0:
         eve_nums.append(numer)
     numer=numer + 1
     
print(eve_nums)

#Q use while loop to calculate sum 

list1 = [8, 3, 4, 5, 6, 7, 9]

accum = 0
itera=0
while itera<len(list1):
    accum=accum+list1[itera]
    itera=itera+1
    print(accum)
    
    
#Q Write a function called stop_at_four that iterates through a list of numbers. Using a while loop, append each number to a new list until the number 4 appears. The function should return the new list.

def stop_at_four():
    list1=[0,1,2,3,4,5,6]
    itera=0
    sumof=0
    list2=[]
    while itera<len(list1):
        if itera<4:
            list2.append(list1[itera])
        itera=itera+1
    return list2
stop_at_four()


def stop_at_four(x):
    list1=x
    itera=0
    sumof=0
    list2=[]
    while itera<len(list1):
        if itera<4:
            list2.append(list1[itera])
        itera=itera+1
    return list2
list1=[0,1,2,3,4,5,6]
stop_at_four(list1)  
    
    
    
    
def funnodup(x):
    my_list=x
    my_list2=[]
    for item in my_list:
        if item in my_list2:
            print('nothing')
        else:
            my_list2.append(item)
    return my_list2


list1=[1,2,2,3,4,5,5,5,6]

funnodup(list1)
        
            
    
    
    
    
    
    
    
    
    