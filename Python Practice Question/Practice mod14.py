# -*- coding: utf-8 -*-
"""
Created on Wed Jun 10 15:30:02 2020

@author: aftab
"""

#Q1
'''
The dictionary Junior shows a schedule for a junior year semester. 
The key is the course name and the value is the number of credits. 
Find the total number of credits taken this semester and assign it to the variable credits. 
Do not hardcode this – use dictionary accumulation!
'''
Junior = {'SI 206':4, 'SI 310':4, 'BL 300':3, 'TO 313':3, 'BCOM 350':1, 'MO 300':3}
total_creadit=0
for key in Junior:
    total_creadit=total_creadit+Junior[key]
print(total_creadit)
credits=total_creadit
print(credits)

#Q2   
'''
Create a dictionary, freq, that displays each character in string str1
as the key and its frequency as the value.
''' 
str1 = "peter piper picked a peck of pickled peppers"

freq={}
for item in str1:
    if item not in freq:
        freq[item]=0
    freq[item]=freq[item]+1
print(freq)
    
#Q3
'''
Provided is a string saved to the variable name s1. Create a dictionary 
named counts 
that contains each letter in s1 and the number of times it occurs.
'''
s1 = "hello"

counts ={}
for item in s1:
    if item not in counts :
        counts [item]=0
    counts [item]=counts [item]+1
print(counts )
    
#Q4
'''
Create a dictionary, freq_words, that contains 
each word in string str1 as the key and its frequency as the value.

'''
str1 = "I wish I wish with all my heart to fly with dragons in a land apart"
str11=str1.split()
freq_words={}
for item in str11:
    if item not in freq_words:
        freq_words[item]=0
    freq_words[item]=freq_words[item]+1
print(freq_words)


#Q5
'''
Create a dictionary called wrd_d from the string sent, 
so that the key is a word 
and the value is how many times you have seen that word.
'''

sent = "Singing in the rain and playing in the rain are two entirely different situations but both can be good"

str11=sent.split()
wrd_d={}
for item in str11:
    if item not in wrd_d:
        wrd_d[item]=0
    wrd_d[item]=wrd_d[item]+1
print(wrd_d)


#Q6
'''
Create the dictionary characters that shows each character from the string sally 
and its frequency. Then, find the most frequent letter based on the dictionary.
Assign this letter to the variable best_char.
'''
sally = "sally sells sea shells by the sea shore"

characters={}
for item in sally:
    if item not in characters:
        characters[item]=0
    characters[item]=characters[item]+1
print(characters)

keys=list(characters.keys())
max_value=characters[keys[0]]
best_char=keys[0]
print(max_value)
for key in keys:
   #print('key..',key)
   if max_value<characters[key]:
       max_value=characters[key]
       print('key..',key)
       best_char=key

print(best_char)

#Q7
'''
Find the least frequent letter. Create the dictionary characters 
that shows each character from string sally and its frequency. 
Then, find the least frequent letter in the string and assign the letter to the variable worst_char.
'''
sally = "sally sells sea shells by the sea shore and by the road"

characters={}
for item in sally:
    if item not in characters:
        characters[item]=0
    characters[item]=characters[item]+1
print(characters)

keys=list(characters.keys())
min_value=characters[keys[0]]
worst_char=keys[0]

for key in keys:
   #print('key..',key)
   if min_value>characters[key]:
       min_value=characters[key]
       print('key..',key)
       worst_char=key

print(worst_char)


#Q8
'''
Create a dictionary named letter_counts that contains each letter 
and the number of times it occurs in string1. 
Challenge: Letters should not be counted separately as upper-case and lower-case. 
Intead, all of them should be counted as lower-case.
'''
string1 = "There is a tide in the affairs of men, Which taken at the flood, leads on to fortune. Omitted, all the voyage of their life is bound in shallows and in miseries. On such a full sea are we now afloat. And we must take the current when it serves, or lose our ventures."
string11=string1.lower()

letter_counts={}
for item in string11:
    if item not in letter_counts:
        letter_counts[item]=0
    letter_counts[item]=letter_counts[item]+1
print(letter_counts)

#Q9
'''
Create a dictionary called low_d that keeps track of all the characters in the string p and notes how many times each character was seen.
Make sure that there are no repeats of characters as keys, such that “T” and “t” are both seen as a “t” for example.
'''
p = "Summer is a great time to go outside. You have to be careful of the sun though because of the heat."


string11=p.lower()
low_d={}
for item in string11:
    if item not in low_d:
        low_d[item]=0
    low_d[item]=low_d[item]+1
print(low_d)




















