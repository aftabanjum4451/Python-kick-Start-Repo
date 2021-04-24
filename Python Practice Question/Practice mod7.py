# -*- coding: utf-8 -*-
"""
Created on Thu Jun  4 11:14:40 2020

@author: aftab
"""
import numpy as np
#Q1
'''
Exercise Question 1: Given a Python list you should be able to display Python list in the following order
aLsit = [100, 200, 300, 400, 500]
reverse the list
'''
#1st solution
aLsit = [100, 200, 300, 400, 500]
aLsit.reverse()
print(aLsit)

#2nd solution 
aLsit = [0, 2, 3, 4, 5,6]
print(aLsit[::-1])# reverse orderig list 
print(aLsit[::2])# extarct numbers whos on even index
print(aLsit[::3])#itervative on 3rd index 

#3rd solution
''' without using buildin function'''

aLsit = [100, 200, 300, 400, 500]
length_alist=len(aLsit)
print(length_alist)

new_list=[0] * length_alist
print(new_list)

print(aLsit[4])

for i in range(length_alist):
    new_list[i]=(aLsit[(length_alist-1)-i])
    print('run ')
print(new_list)
    
#4th solution
aLsit = [100, 200, 300, 400, 500]
new_list=[]
for i in aLsit:
    new_list.insert(0,i)
print(new_list)

#Q2
'''
Exercise Question 2: Concatenate two lists index-wise
list1 = ["M", "na", "i", "Ke"] 
list2 = ["y", "me", "s", "lly"]

'''
#1 solution 
list1 = ["M", "na", "i", "Ke"] 
list2 = ["y", "me", "s", "lly"]
list3=[]
for i in range(len(list1)):
    list3.append(list1[i]+list2[i])
   
print(list3)

#2 solution
list1 = ["M", "na", "i", "Ke"] 
list2 = ["y", "me", "s", "lly"]
list3 = [i + j for i, j in zip(list1, list2)]
print(list3)

#Q3
'''
Exercise Question 3: Given a Python list. 
Turn every item of a list into its square
'''
#1 solution
aList = [1, 2, 3, 4, 5, 6, 7]
new_list=[]
for i in aList:
    new_list.append(i**2) 
print(new_list)

# 2nd solution 
aList = [1, 2, 3, 4, 5, 6, 7]
aList =  [x * x for x in aList]
print(aList)
    

#Q4
'''
Concatenate two lists in the following order
list1 = ["Hello ", "take "]
list2 = ["Dear", "Sir"]
output: 
['Hello Dear', 'Hello Sir', 'take Dear', 'take Sir']    
'''
#1solution 
list1 = ["Hello ", "take "]
list2 = ["Dear", "Sir"]

list3=[]
for i in range(len(list1)):
    for k in range(len(list2)):
        list3.append(list1[i]+' '+list2[k])
print(list3)

#Q5
'''Given a two Python list. Iterate both lists simultaneously
such that list1 should display item in original order and list2 in reverse order

list1 = [10, 20, 30, 40]
list2 = [100, 200, 300, 400]

output

10 400
20 300
30 200
40 100
'''
#1 solution 
list1 = [10, 20, 30, 40]
list2 = [100, 200, 300, 400]
length_oflist2=len(list2)

for i in range(len(list1)):
     #print(list1[i]), print(list2[(length_oflist2-1)-i])
     print(list1[i], list2[(length_oflist2-1)-i])
    
#2nd solution 
list1 = [10, 20, 30, 40]
list2 = [100, 200, 300, 400]

for x, y in zip(list1, list2[::-1]):
    print(x, y)

#Q6
'''
Question 6: Remove empty strings from the list of strings

list1 = ["Mike", "", "Emma", "Kelly", "", "Brad"]

'''
list1 = ["Mike", "", "Emma", "Kelly", "", "Brad"]
for item in list1:
    if item=="":
        list1.remove(item)
print(list1)

#Q7
'''
Question 7: Add item 7000 after 6000 in the following Python List
list1 = [10, 20, [300, 400, [5000, 6000], 500], 30, 40]
'''        
list1 = [10, 20, [300, 400, [5000, 6000], 500], 30, 40]
list1[2][2].append(7000)
print(list1)

#Q8
'''
Given a nested list extend it with adding sub list ["h", "i", "j"] in a 
such a way that it will look like the following list

list1 = ["a", "b", ["c", ["d", "e", ["f", "g"], "k"], "l"], "m", "n"]
output:
    ['a', 'b', ['c', ['d', 'e', ['f', 'g', 'h', 'i', 'j'], 'k'], 'l'], 'm', 'n']
'''

list1 = ["a", "b", ["c", ["d", "e", ["f", "g"], "k"], "l"], "m", "n"]

temp_list=["h", "i", "j"]

for item in temp_list:
    list1[2][1][2].append(item)
    print(list1)
print(list1)

#2nd solution by using extend function 
list1 = ["a", "b", ["c", ["d", "e", ["f", "g"], "k"], "l"], "m", "n"]
subList = ["h", "i", "j"]

list1[2][1][2].extend(subList)
print(list1)

#Q9
'''
Question 9: Given a Python list, find value 20 in the list, 
and if it is present, replace it with 200.
Only update the first occurrence of a value
list1 = [5, 10, 15, 20, 25, 50, 20]
'''    
list1 = [5, 10, 15, 20, 25, 50, 20]
index=list1.index(20)
list1[index]=200
print(list1)

#Q10
'''
Given a Python list, remove all occurrence of 20 from the list

list1 = [5, 20, 15, 20, 25, 50, 20]
'''
list1 = [5, 20, 15, 20, 25, 50, 20]
for item in list1:
    if item==20:
        list1.remove(item)
print(list1)

#2nd solution 
list1 = [5, 20, 15, 20, 25, 50, 20]

def removeValue(sampleList, val):
   return [value for value in sampleList if value != val]
resList = removeValue(list1, 20)
print(resList)

#Q11
'''
Take a list, say for example this one:

a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
and write a program that prints out 
all the elements of the list that are less than 5.


    

'''
a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]

for item in a:
    if item<5:
        print(item)
        
#1)
'''
1)Instead of printing the elements one by one, make 
a new list that has all the elements less 
than 5 from this list in it and print out this new list.
'''
a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
temp_list=[]
for item in a:
    if item<5:
        temp_list.append(item)
print(temp_list)
        
#2)
''' 
Ask the user for a number and return a list that contains only elements 
from the original list a that are smaller than that number given by the user.              
'''     
a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]       
    
unser_number=input('please enter a number')
temp_list=[]
for item in a:
    if item<int(unser_number):
        temp_list.append(item)
print(temp_list)    


#Q 12
'''
Take two lists, say for example these two:

a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
b = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]
and write a program that returns a list that contains only 
the elements that are common between the lists (without duplicates). 
Make sure your program works on two lists of different sizes.

Extras:

Randomly generate two lists to test this
Write this in one line of Python 
(don’t worry if you can’t figure this out at this point - we’ll get to it soon)

'''    
a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89,24,7,8,7,8]
b = [1,1,2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]
tem_list=[]
for item in b:
    if item in a:
        if item in tem_list:
            print('not apply')
        else:
            tem_list.append(item)
            
        
print(tem_list)

#1)       
        














