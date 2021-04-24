# -*- coding: utf-8 -*-
"""
Created on Tue Aug 25 12:59:29 2020

@author: aftab
"""
# list comprehension 

'''[ expression for item in list  if condition ]'''

things = [2, 5, 9]

yourlist = [value * 2 for value in things]

print(yourlist) 

#
city_name=['lahore','karachi','islamabad','multan','fsb']
upper_leter=[city.upper() for city in city_name]
print(upper_leter)

#assign name contain 'a' from above list 

city_name=['lahore','karachi','islamabad','multan','fsb']

name_word=[ city for city in city_name if 'a'in city]

print(name_word)

#
'''

Write code to assign to the variable compri all the values of 
the key name in any of the sub-dictionaries in the dictionary tester.
Do this using a list comprehension.

'''
tester = {'info': [{"name": "Lauren", 'class standing': 'Junior', 'major': "Information Science"},{'name': 'Ayo', 'class standing': "Bachelor's", 'major': 'Information Science'}, {'name': 'Kathryn', 'class standing': 'Senior', 'major': 'Sociology'}, {'name': 'Nick', 'class standing': 'Junior', 'major': 'Computer Science'}, {'name': 'Gladys', 'class standing': 'Sophomore', 'major': 'History'}, {'name': 'Adam', 'major': 'Violin Performance', 'class standing': 'Senior'}]}

#with out list compreshnsion 
compri=[]
for item1 in tester.keys():
    for item2 in tester[item1]:
        for item3 in item2.keys():
            if item3=='name':
                compri.append((item2[item3]))
print(compri)

#now with list comprehension 
tester = {'info': [{"name": "Lauren", 'class standing': 'Junior', 'major': "Information Science"},{'name': 'Ayo', 'class standing': "Bachelor's", 'major': 'Information Science'}, {'name': 'Kathryn', 'class standing': 'Senior', 'major': 'Sociology'}, {'name': 'Nick', 'class standing': 'Junior', 'major': 'Computer Science'}, {'name': 'Gladys', 'class standing': 'Sophomore', 'major': 'History'}, {'name': 'Adam', 'major': 'Violin Performance', 'class standing': 'Senior'}]}

inner_list=tester['info']

print(d)

import json 

print(json.dumps(d, indent=2))

'''[<transform_ex> for variiance in <sequence> if <filter_expression>]'''

word_name1=[d['name'] for d in inner_list ]

print(word_name1)

# write function take string and return length of thise string have length at least 4
def final_fun(list1):
    long_length=[]
    for item in list1:
        if len(item)>=4:
            long_length.append(item) 
    return long_length
            
list1=['lahore','china','ali','fsb','love from lahore']

final_fun(list1)

# with list comprehension

def long_length(st):
    return [item for item in st if len(item)>=4]


long_length(['lahore','china','ali','fsb','love from lahore'])

# using filter function 

def leng_deter(st):
    if len(st)>=4:
        return st

def map_fun(list1):
    expression=map(leng_deter, list1)
    return list(expression)

map_fun(['lahore','china','ali','fsb','love from lahore'])      
list1=['lahore','china','ali','fsb','love from lahore']
for item in list1:
    print(string_leng(item))
    
    









    










            
            
            
        
        
             
      
    
            
            
        
        
        
        
        
        
    











