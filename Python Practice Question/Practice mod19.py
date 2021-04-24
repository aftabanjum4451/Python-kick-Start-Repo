# -*- coding: utf-8 -*-
"""
Created on Mon Aug 24 15:18:22 2020

@author: aftab
"""

#Q
'''
The variable nested contains a nested list. Assign ‘snake’ to the variable output using indexing.
'''

nested = [['dog', 'cat', 'horse'], ['frog', 'turtle', 'snake', 'gecko'], ['hamster', 'gerbil', 'rat', 'ferret']]

output=nested[1][2]
print(output)

#Q

'''
Below, a list of lists is provided. 
Use in and not in tests to create variables with Boolean values. 
See comments for further instructions.

'''

lst = [['apple', 'orange', 'banana'], [5, 6, 7, 8, 9.9, 10], ['green', 'yellow', 'purple', 'red']]

#Test to see if 'yellow' is in the third list of lst. Save to variable ``yellow``
if 'yellow' in lst[2]:
    yellow=True
else:
    yellow=False
#Test to see if 4 is in the second list of lst. Save to variable ``four``
if 4 in lst[1]:
    four=True
else:
    four=False
#Test to see if 'orange' is in the first element of lst. Save to variable ``orange``
if 'orange' in lst[0]:
    orange=True
else:
    orange=False


# Q
'''
Below, we’ve provided a list of lists. Use in statements to 
create variables with Boolean values - 
see the ActiveCode window for further directions.
'''
L = [[5, 8, 7], ['hello', 'hi', 'hola'], [6.6, 1.54, 3.99], ['small', 'large']]

# Test if 'hola' is in the list L. Save to variable name test1
if 'hola' in L:
    test1=True
else:
    test1=False
# Test if [5, 8, 7] is in the list L. Save to variable name test2
if [5, 8, 7] in L:
    test2=True
else:
    test2=False

# Test if 6.6 is in the third element of list L. Save to variable name test3

if 6.6 in L[2]:
    test3=True
else:
    test3=False

#Q
'''
Below, we have provided a nested dictionary. 
Index into the dictionary to create variables 
that we have listed in the ActiveCode window.

'''
sports = {'swimming': ['butterfly', 'breaststroke', 'backstroke', 'freestyle'], 'diving': ['springboard', 'platform', 'synchronized'], 'track': ['sprint', 'distance', 'jumps', 'throws'], 'gymnastics': {'women':['vault', 'floor', 'uneven bars', 'balance beam'], 'men': ['vault', 'parallel bars', 'floor', 'rings']}}


for item1 in sports.keys():
    for item2 in sports['swimming']:
        if item2=='backstroke':
            v1=item2
print(v1)
        
# Assign the string 'backstroke' to the name v1
for item1 in sports.keys():
    for item2 in sports[item1]:
        if item2=='backstroke':
            v1=item2
print(v1)

# Assign the string 'platform' to the name v2
for item1 in sports.keys():
    for item2 in sports[item1]:
        if item2=='platform':
            v2=item2
print(v2)

# Assign the list ['vault', 'floor', 'uneven bars', 'balance beam'] to the name v3
for item1 in sports.keys():
    for item2 in sports[item1]:
        if item2==['vault', 'floor', 'uneven bars', 'balance beam']:
            v3=item2
print(v3)

# Assign the string 'rings' to the name v4

for item1 in sports.keys():
    for item2 in sports[item1]:
        print(item2)
        
            if item3=='rings':
                v4=item3
print(v4)

#Q
'''
Given the dictionary, nested_d, 
save the medal count for the USA from all three Olympics in the dictionary
 to the list US_count.
'''
nested_d = {'Beijing':{'China':51, 'USA':36, 'Russia':22, 'Great Britain':19},
            'London':{'USA':46, 'China':38, 'Great Britain':29, 'Russia':22}, 
            'Rio':{'USA':35, 'Great Britain':22, 'China':20, 'Germany':13}}


US_count=[]
for item1 in nested_d.keys():
    for item2 in nested_d[item1]:
        if item2 =='USA':
            US_count.append(nested_d[item1][item2])
            
print(US_count)



#Q
nested_d = {'Beijing':{'China':51, 'USA':36, 'Russia':22, 'Great Britain':19},
            'London':{'USA':46, 'China':38, 'Great Britain':29, 'Russia':22}, 
            'Rio':{'USA':35, 'Great Britain':22, 'China':20, 'Germany':13}}

london_gold = 0

for item1 in nested_d.keys():
    if item1=='London':
         for item2 in nested_d[item1]:
             if item2 =='Great Britain':
                 london_gold=london_gold+nested_d[item1][item2]
print(london_gold)
        
            
        
   

#Q
'''
Iterate through the contents of l_of_l and assign 
the third element of sublist to a new list called third.

'''

l_of_l = [['purple', 'mauve', 'blue'], ['red', 'maroon', 'blood orange', 'crimson'], ['sea green', 'cornflower', 'lavender', 'indigo'], ['yellow', 'amarillo', 'mac n cheese', 'golden rod']]

third=[]

for i in range(len(l_of_l)):
    print('northing')
    for k in range(len(l_of_l[i])):
        if k==2:
            third.append(l_of_l[i][k])
print(third)



#Q

'''
Given below is a list of lists of athletes. 
Create a list, t, that saves only the athlete’s name 
if it contains the letter “t”. If it does not contain 
the letter “t”, save the athlete name into list other.

'''
athletes = [['Phelps', 'Lochte', 'Schooling', 'Ledecky', 'Franklin'], ['Felix', 'Bolt', 'Gardner', 'Eaton'], ['Biles', 'Douglas', 'Hamm', 'Raisman', 'Mikulak', 'Dalton']]

t=[]
other=[]           
for item1 in  athletes:
    for item2 in item1:
        if 't'in item2:
            t.append(item2)
        else:
            other.append(item2)

print(t)
print(other)            
            
   
        

#Q
# Check to see if the string data is a key in nested, if it is, assign True to the variable data, otherwise assign False.
if 'data' in nested:
    data = True
else:
    data = False
# Check to see if the integer 24 is in the value of the key data, if it is then assign to the variable twentyfour the value of True, otherwise False.
if 24 in nested:
    twentyfour = True
else:
    twentyfour = False
# Check to see that the string 'whole' is not in the value of the key window. If it's not, then assign to the variable whole the value of True, otherwise False.
if 'whole' in nested:
    whole = True
else:
    whole = False
# Check to see if the string 'physics' is a key in the dictionary nested. If it is, assign to the variable physics, the value of True, otherwise False.
if 'physics' in nested:
    physics = True
else:
    physics = False















            
            
        
        
        
        
        
    
    






