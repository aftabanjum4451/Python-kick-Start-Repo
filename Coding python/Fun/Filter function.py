# -*- coding: utf-8 -*-
"""
Created on Tue Aug 25 12:19:56 2020

@author: aftab
"""
'''
Note: filter(), map(), both return objec
so we need to convert then into list or 
any other type according to required choice 
'''
        
#filer function for even number   
def filer_fun(nums):
    a=filter(lambda num: num % 2== 0,nums)
    return list(a)

num_list=[1,2,4,5,6,7]
print(filer_fun(nums_lis))

# without lambda function 
def num(num):
    if num % 2==0:
        return num
    
def filer_fun1(nums):
    a=filter(num,nums)
    return list(a)

num_list=[1,2,4,5,6,7]
print(filer_fun1(num_list))

'''
Write code to assign to the variable filter_testing all the elements 
in lst_check that have a w in them using filter.
'''
lst_check = ['plums', 'watermelon', 'kiwi', 'strawberries', 'blueberries', 'peaches', 'apples', 'mangos', 'papaya']


def fun_checkletter(st):
    if 'w'in st:
        return st

def filer_lettercheck(list1):
    filter_testing=filter(fun_checkletter,list1)
    return list(filter_testing)

filer_lettercheck(lst_check)


'''
Using filter, filter lst so that it only contains words containing 
the letter “o”. Assign to variable lst2. Do not hardcode this.

'''
lst = ["witch", "halloween", "pumpkin", "cat", "candy", "wagon", "moon"]


def fun_checkletter(st):
     if 'o'in st:
        return st

def filer_lettercheck(list1):
    filter_testing=filter(fun_checkletter,list1)
    return list(filter_testing)

filer_lettercheck(lst)


#lambda way 
def filer_lettercheck(list1):
    filter_testing=filter(lambda word: 'o'in word,list1)
    return list(filter_testing)

filer_lettercheck(lst)






