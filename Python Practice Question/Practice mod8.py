# -*- coding: utf-8 -*-
"""
Created on Wed Jun 10 11:41:27 2020

@author: aftab
"""
#Q1
medals={'gold':33, 'silver':17, 'bronze':12}
print(medals)

olympics={'gold':7,'silver':8, 'bronze':6}
print(olympics)

#Q2
places = {"Australia":2000, "Greece":2004, "China":2008, "England":2012}

places['Brazil']= 2016
print(places)

#q3
medal_events = {'Shooting': 7, 'Fencing': 4, 'Judo': 2, 'Swimming': 3, 'Diving': 2}
events=list(medal_events.keys())
print(events)

#Q4
'''
Provided is a string saved to the variable name sentence. 
Split the string into a list of words, 
then create a dictionary that contains each word and the number of times it occurs. 
Save this dictionary to the variable name word_counts.
'''
sentence = "The dog chased the rabbit into the forest but the rabbit was too quick."

my_list=sentence.split()

dic={}

for item in my_list:
    if item not in dic:
        dic[item]=0
    dic[item]=dic[item]+1
    
print(dic)
        

#Q5
'''
Create a dictionary called char_d from the string stri,
so that the key is a character and the value is how many times it occurs.
'''
stri = "what can I do"

#my_list1=stri.split()

dic1={}

for item in stri:
    if item not in dic1:
        dic1[item]=0
    dic1[item]=dic1[item]+1
    
print(dic1)
char_d=dic1
print(dic1)

#Q  Write a function named same that takes a string as input, and simply returns that string.

def decision(str1):
    if len(str1)>17:
        return ('This is a long string')
    else :
        return ('This is a short string')
    
    

decision('hello oakistan i love you but i cant get in side ')


















        





    









