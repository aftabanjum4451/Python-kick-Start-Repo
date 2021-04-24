# -*- coding: utf-8 -*-
"""
Created on Mon Sep 21 09:57:23 2020

@author: aftab
"""
## exception handling 
# this below code can handle can except any type of error 
try:
   # statememt
   #stamenetn2
except Exception  :
    print('the error is here')



try:
    items = ['a', 'b']
    third = items[2]
    print("This won't print")
except Exception:
    print("got an error")

print("continuing")


try:
    items = ['a', 'b']
    third = items[2]
    print("This won't print")
except IndexError:
    print("error 1")

print("continuing")

try:
    x = 5
    y = x/0
    print("This won't print, either")
except ZeroDivisionError:
    print("error 2")


print("continuing again")


# to see the exception type 
try:
    items = ['a', 'b']
    third = items[2]
    print("This won't print")
except Exception as e:
    print("got an error")
    print(e)
        


#

'''
Below, we have provided a list of tuples that consist of student names, 
final exam scores, and whether or not they will pass the class. 
For some students, the tuple does not have a third element because
 it is unknown whether or not they will pass. Currently, 
 the for loop does not work. Add a try/except clause so the code runs 
 without an error - if there is no third element in the tuple, no 
 changes should be made to the dictionary.
'''
students = [('Timmy', 95, 'Will pass'), ('Martha', 70), ('Betty', 82, 'Will pass'), ('Stewart', 50, 'Will not pass'), ('Ashley', 68), ('Natalie', 99, 'Will pass'), ('Archie', 71), ('Carl', 45, 'Will not pass')]

passing = {'Will pass': 0, 'Will not pass': 0}

for tup in students:
    try:
        if tup[2] == 'Will pass':
            passing['Will pass'] += 1
        
        elif tup[2] == 'Will not pass':
            passing['Will not pass'] += 1
    except Exception:
          pass
        
    
print(passing)

#
'''
Below, we have provided code that does not run. 
Add a try/except clause so the code runs without errors. 
If an element is not able to undergo the addition operation, 
the string ‘Error’ should be appended to plus_four.
'''
nums = [5, 9, '4', 3, 2, 1, 6, 5, '7', 4, 3, 2, 6, 7, 8, '0', 3, 4, 0, 6, 5, '3', 5, 6, 7, 8, '3', '1', 5, 6, 7, 9, 3, 2, 5, 6, '9', 2, 3, 4, 5, 1]

plus_four = []

for num in nums:
    try:
        plus_four.append(num+4)
    except Exception as e:
        plus_four.append(e)
        
print(plus_four)       
  
