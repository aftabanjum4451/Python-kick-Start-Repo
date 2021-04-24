# -*- coding: utf-8 -*-
"""
Created on Mon Aug 24 11:10:52 2020

@author: aftab
"""


#shallow copies 
'''
during  shallow copies if we change in one list 
the change can also be seen in the copied list version 
'''
original = [['dogs', 'puppies'], ['cats', "kittens"]]
copied_version = original[:]
print(copied_version)
print(copied_version is original)
print(copied_version == original)
original[0].append(["canines"])
print(original)
print("-------- Now look at the copied version -----------")
print(copied_version)



list1=[1,2,3,4,5,6]
copied_list1=list1[:]
print(copied_list1 is list1)
print(copied_list1 == list1)
list1[0]='hello'
print('first list ',list1)
print('2nd list ',copied_list1)



#sove the shallow copy problem by loop
original = [['dogs', 'puppies'], ['cats', "kittens"]]
copied_outer_list = []
for inner_list in original:
    copied_inner_list = []
    for item in inner_list:
        copied_inner_list.append(item)
    copied_outer_list.append(copied_inner_list)
print(copied_outer_list)
original[0].append(["canines"])
print(original)
print("-------- Now look at the copied version -----------")
print(copied_outer_list)


#same thing can do by using copy libray and deepcopy.() method 
import copy
original = [['canines', ['dogs', 'puppies']], ['felines', ['cats', 'kittens']]]
shallow_copy_version = original[:]
deeply_copied_version = copy.deepcopy(original)
original.append("Hi there")
original[0].append(["marsupials"])
print("-------- Original -----------")
print(original)
print("-------- deep copy -----------")
print(deeply_copied_version)
print("-------- shallow copy -----------")
print(shallow_copy_version)






 







