# -*- coding: utf-8 -*-
"""
Created on Fri Jun  5 17:38:23 2020

@author: aftab
"""
#Q2
cawdra = ['candy', 'daisy', 'pear', 'peach', 'gem', 'crown']
t = 0
for elem in cawdra:
    t = t + len(elem)
print(t)

#Q2
'''
Currently there is a string called str1.
Write code to create a list called chars which should contain the characters from str1. 
Each character in str1 should be its own element in the list chars.
'''


chars=[]
str1 = "I love python"
for k in range(len(str1)):
    chars.append((str1[k]))
print(chars)


'''.........week4 assignmet 4..........'''

#Q
app=[]
ael = "python!"
for item in ael:
    app.append(item)
    
#Q

wrds = ["end", 'work', "play", "start", "walk", "look", "open", "rain", "learn", "clean"]
past_wrds=[]
for item in wrds:
    past_wrds.append(item+'ed')
print(past_wrds)
    








    
    


