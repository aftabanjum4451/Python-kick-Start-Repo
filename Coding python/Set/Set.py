# -*- coding: utf-8 -*-
"""
Created on Mon Aug 17 12:31:27 2020

@author: aftab
"""
#set creation 
my_set={1,2,4,5,4,4,5,8} # set ony give non duplicate vale and neglet non duplicate values
print(my_set)

# Q can we remove duplicate value from list 

list1=[1,2,2,3,4,4,4,5,8,7]

print(set(list1))

#differnce function to check the differnce between two given set

my_set={1,2,3,4,5,6}
my_2nd_set={4,5,6,7,8,9}

print(my_set.difference(my_2nd_set))

# differnce update function 

print(my_set.difference_update(my_2nd_set))
print(my_set)

# intersection function 

print(my_set.intersection(my_2nd_set))
print(my_set)

# isdisjoint function 

print(my_set.isdisjoint(my_2nd_set))
print(my_set)

#union
print(my_set.union(my_2nd_set))


#subset 

print(my_set.issubset(my_2nd_set))

# super subet
print(my_set.issuperset(my_2nd_set))






























