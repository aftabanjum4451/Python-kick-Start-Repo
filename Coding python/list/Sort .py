# -*- coding: utf-8 -*-
"""
Created on Sat Aug 22 12:22:08 2020

@author: aftab
"""

#two method of soting 
#sort()
#sorted()


#sort()
list1=[1,2,0,3,4,5,25,6,7,8,40,9]

print(list1.sort())
print(list1)

#sorted 

list2=[100,2,0,3,4,5,25,6,7,8,40,90,]

sorted(list2)

print(sorted(list2, reverse=True))

print(list2)

#string sort
print(sorted('apple'))

print('apple'.sort())

#absolute 

L1 = [1, 7, 4, -2, 3]

def absolute(x):
    if x >= 0:
        return x
    else:
        return -x

print(absolute(3))
print(absolute(-119))

for y in L1:
    print(absolute(y))
    
#absoute function passing in an othe function sort as key value
L1 = [1, 7, 4, -2, 3]

def absolute(x):
    print("--- figuring out what to write on the post-it note for " + str(x))
    if x >= 0:
        return x
    else:
        return -x

print("About to call sorted")
L2 = sorted(L1, key=absolute)
print("Finished execution of sorted")
print(L2)
   
#Q

'''
  You will be sorting the following list by each element’s second letter,
  a to z. Create a function to use when sorting, called second_let. 
  It will take a string as input and return the second letter of that string. 
  Then sort the list, create a variable called sorted_by_second_let and assign
  the sorted list to it. Do not use lambda.   
    
'''  
    
ex_lst = ['hi', 'how are you', 'bye', 'apple', 'zebra', 'dance']



def second_let(list2):
    tem_liat=[]
    sorted_by_second_let=[]
    for item in list2:
        tem_liat.append(item[1])
    sorted_by_second_let=sorted(tem_liat)
    return sorted_by_second_let

   
second_let(ex_lst)

  
nums = ['1450', '33', '871', '19', '14378', '32', '1005', '44', '8907', '16']

nums=['s','t','w']

def last_char(nums):
    list2=[]
    nums_sorted=[]
    for item in nums:
        list2.append(item[-1])
    nums_sorted=sorted(list2, reverse=True)
    return nums_sorted 

last_char(nums)  


#sorting dictionary 
L = ['E', 'F', 'B', 'A', 'D', 'I', 'I', 'C', 'B', 'A', 'D', 'D', 'E', 'D']

d = {}
for x in L:
    if x in d:
        d[x] = d[x] + 1
    else:
        d[x] = 1

y = sorted(d.keys(), key=lambda k: d[k], reverse=True)
for k in y:
    print("{} appears {} times".format(k, d[k]))


#Q Sort the following dictionary based on the keys so that they are sorted a to z. Assign the resulting value to the variable sorted_keys.

dictionary = {"Flowers": 10, 'Trees': 20, 'Chairs': 6, "Firepit": 1, 'Grill': 2, 'Lights': 14}
sorted(dictionary.keys())
    
#Sort the following dictionary’s keys based on the value from highest to lowest. Assign the resulting value to the variable sorted_values.
dictionary = {"Flowers": 10, 'Trees': 20, 'Chairs': 6, "Firepit": 1, 'Grill': 2, 'Lights': 14}

y=sorted(dictionary.keys(), key=lambda k:dictionary[k],reverse=True)

for k in y:
    print('{} apprear {}time in dictionary'.format(k,dictionary[k]))

#tuple sorting 
tups = [('A', 3, 2),
        ('C', 1, 4),
        ('B', 3, 1),
        ('A', 2, 4),
        ('C', 1, 2)]
for tup in sorted(tups):
    print(tup)


fruits = ['peach', 'kiwi', 'apple', 'blueberry', 'papaya', 'mango', 'pear']
new_order = sorted(fruits, key=lambda fruit_name: (len(fruit_name), fruit_name))
for fruit in new_order:
    print(fruit)


fruits = ['peach', 'kiwi', 'apple', 'blueberry', 'papaya', 'mango', 'pear']
new_order = sorted(fruits, key=lambda fruit_name: (len(fruit_name), fruit_name), reverse=True)
for fruit in new_order:
    print(fruit)
    
    
fruits = ['peach', 'kiwi', 'apple', 'blueberry', 'papaya', 'mango', 'pear']
new_order = sorted(fruits, key=lambda fruit_name: (-len(fruit_name), fruit_name))
for fruit in new_order:
    print(fruit)









    
    
    
    
    
    
    
    
    
    
    
    
    
    