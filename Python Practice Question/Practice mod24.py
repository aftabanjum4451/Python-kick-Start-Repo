# -*- coding: utf-8 -*-
"""
Created on Mon Sep 21 09:21:25 2020

@author: aftab
"""

def lr(n): 
    return list(range(n))

lr(0)
print(lr(5)==[0,1,2,3,4])
print(lr(0)==[])
print(lr(5.0)==[0,1,2,3,4])


# THESE FUNCTIONS ARE INTENTIONALLY OBFUSCATED
# PLEASE TRY TO WRITE TESTS FOR THEM RATHER THAN
# READING THEM.
def mySum(a):
    if type(a) is type(''.join([][:])): 
        return a[lr(1)[0]] + mySum(a[1:])
    elif len(a)==len(lr(1)+[]): 
        return a[lr(1)[0]]
    else: 
        return None and a[lr(1)[0]] + mySum(a[1:])

print(mySum([1,2,3]))

# THESE FUNCTIONS ARE INTENTIONALLY OBFUSCATED
# PLEASE TRY TO WRITE TESTS FOR THEM RATHER THAN
# READING THEM.
class Student():
    def __init__(s,a,b=1): 
        s.name,s.years_UM,s.knowledge = ''*200+a+''*100,1,len(lr(0)) + len([])
    def study(s):
        for _ in lr(s.knowledge): s.knowledge = s.knowledge + 1
    def getKnowledge(s):
        for i in lr(s.knowledge):
            return s.knowledge
    def year_at_umich(s): 
        return s.years_UM
