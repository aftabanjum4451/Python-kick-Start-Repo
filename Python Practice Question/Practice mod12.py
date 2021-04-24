# -*- coding: utf-8 -*-
"""
Created on Mon Aug 10 18:46:47 2020

@author: aftab
"""


#Q Write a function called int_return that takes an integer as input and returns the same integer.
def int_return(a):
    return a

int_return(25)


#q Write a function called add that takes any number as its input and returns that sum with 2 added.
def add(a):
    return a+2

add(25)

#Q Write a function called change that takes any string, adds “Nice to meet you!” to the end of the argument given, and returns that new string.

def change(str1):
    resulttemp='{}Nice to meet you!'.format(str1)
    return resulttemp


change('hello')

#Q Write a function, accum, that takes a list of integers as input and returns the sum of those integers.

def accum(lst):
    sumresult=0
    for item in lst:
        sumresult=sumresult+item
    return sumresult


accum([1,6,7,88]) 

#Q Write a function, length, that takes in a list as the input. If the length of the list is greater than or equal to 5, return “Longer than 5”. If the length is less than 5, return “Less than 5”.

def length(lst):
    if len(lst)>=5:
        return ('Longer than 5')
    else:
        return ('Less than 5')


length([1,6,7,88]) 


#QYou will need to write two functions for this problem. The first function, divide that takes in any number and returns that same number divided by 2. The second function called sum should take any number, divide it by 2, and add 6. It should return this new number. You should call the divide function within the sum function. Do not worry about decimals.

def divide(a):
    return (a/2)
    
def sum(b):
    resultfinal=divide(b)+6
    return resultfinal 

sum(6)


#Q











