# -*- coding: utf-8 -*-
"""
Created on Sun Jun  7 19:06:16 2020

@author: aftab
"""
#Q1
'''
The textfile, travel_plans.txt, contains the summer travel plans for someone with some commentary. 
Find the total number of characters in the file and save to the variable num.
'''

file_obj=open('travel_plans.txt','r')
content=file_obj.read()
num=(len(content))
print(num)

#Q2
'''
We have provided a file called emotion_words.txt that contains lines of words that describe emotions. 
Find the total number of words in the file and assign this value to the variable num_words.
'''

file_obj=open('emotion_words.txt','r')
content=file_obj.read()
temp_content=content.split()
k=0
for item in temp_content:
    print(item)
    k+=1
num_words=k


#Q3
'''
Assign to the variable num_lines the number of lines in the file school_prompt.tx

'''
file_obj=open('school_prompt.txt','r')
content=file_obj.readlines()
print(content)
k=0
for line in content:
    print(line.strip())
    k+=1
num_lines=k
print(num_lines)
    
#Q4
'''    
Assign the first 30 characters of school_prompt.txt as a string to the variable beginning_chars.  
''' 
file_obj=open('school_prompt.txt','r')
content=file_obj.read()[0:31]
print(content)
beginning_chars=content


#Q5
'''
Challenge: Using the file school_prompt.txt, 
assign the third word of every line to a list called three.
'''
file_obj=open('school_prompt.txt','r')
content=file_obj.readlines()
three=[]
for line in content:
    temp_line=line.strip()
    temp_line2=temp_line.split()
    #print(temp_line2[2])
    three.append(temp_line2[2])
    
print(three)
    
#Q6
'''
Challenge: Create a list called emotions that contains 
the first word of every line in emotion_words.txt.

'''
file_obj=open('emotion_words.txt','r')
content=file_obj.readlines()
emotions=[]
for line in content:
    temp_line=line.strip()
    temp_line2=temp_line.split()
    #print(temp_line2[2])
    emotions.append(temp_line2[0])
    
print(emotions)  
    
 
#Q7
'''
Assign the first 33 characters from the textfile, 
travel_plans.txt to the variable first_chars.

'''   
file_obj=open('travel_plans.txt','r')
content=file_obj.read()[0:34]
print(content)
first_chars=content
print(first_chars)    
    
#Q8
'''
Challenge: Using the file school_prompt.txt, if the character ‘p’ is in a word, 
then add the word to a list called p_words.
'''
file_obj=open('school_prompt.txt','r')
content=file_obj.readlines()
p_words=[]
for line in content:
    temp_line=line.strip()
    temp_line2=temp_line.split()
    for word in temp_line2:
        if 'p' in word:
            p_words.append(word)
print(p_words)
        
    #print(temp_line2[2])
    #three.append(temp_line2[2])
    
#print(three)
    

    
    






