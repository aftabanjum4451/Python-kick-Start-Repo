# -*- coding: utf-8 -*-
"""
Created on Sat Aug 22 21:01:18 2020

@author: aftab
"""

# lambda function 
a=lambda x:x+x
print(a(3))

a=lambda x:x+x
print(a(5))

# passing value in lambda 
(lambda x: x + 1)(2)

# fun calling inside of function 
def mult(z):
    return (lambda x:x+z)
resul=mult(5)
print(resul(5))

def sum1(x):
    return lambda s:s*x

b=sum1(7)
b(7)

# lambda function in dictionary and sorting  

states = {"Minnesota": ["St. Paul", "Minneapolis", "Saint Cloud", "Stillwater"],
          "Michigan": ["Ann Arbor", "Traverse City", "Lansing", "Kalamazoo"],
          "Washington": ["Seattle", "Tacoma", "Olympia", "Vancouver"]}


print(sorted(states.keys(), key=lambda state:len(states[state][0])))

#sort by city name S count

states = {"Minnesota": ["St. Paul", "Minneapolis", "Saint Cloud", "Stillwater"],
          "Michigan": ["Ann Arbor", "Traverse City", "Lansing", "Kalamazoo"],
          "Washington": ["Seattle", "Tacoma", "Olympia", "Vancouver"]}


def sort_city_name_count(list1):
    count=0
    for city in list1:
        if city[0]=='S':
            count=count + 1
    return count
            
print(sorted(states.keys(), key=lambda state: sort_city_name_count(states[state]) ))        
        
#sort by number of count letter 
L = ['E', 'F', 'B', 'A', 'D', 'I', 'I', 'C', 'B', 'A', 'D', 'D', 'E', 'D']

d = {}
for x in L:
    if x in d:
        d[x] = d[x] + 1
    else:
        d[x] = 1
y = sorted(d.keys())
for k in y:
    print("{} appears {} times".format(k, d[k]))




        
        
        
        
        
        
        






