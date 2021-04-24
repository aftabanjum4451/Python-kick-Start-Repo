# -*- coding: utf-8 -*-
"""
Created on Sat Aug 22 08:28:46 2020

@author: aftab
"""

'''
Q  Write a function, sublist, that takes in a list of numbers as the parameter. 
In the function, use a while loop to return a sublist of the input list. 
The sublist should contain the same values of the original list up until it reaches the number 5
 (it should not contain the number 5).
'''

def sublist(a):
    list2=a
    list1=[]
    num=0
    while num<len(list2):
        if list2[num]==5:
            break
        else:
            list1.append(list2[num])
            num=num+1
    return list1

temp_list=[1,2,3,4,5,6]
sublist(temp_list)
        


#Q Write a function called check_nums that takes a list as its parameter, and contains a while loop that only stops once the element of the list is the number 7. What is returned is a list of all of the numbers up until it reaches 7.
def check_nums(b):
    templist=b
    lsit_result=[]
    number=0
    while number<len(templist):
        if templist[number]==7:
            break
        else:
            lsit_result.append(templist[number])
            number=number+1
    return lsit_result 

temp_list1=[1,2,3,4,5,6,7,8,9,10]
check_nums(temp_list1)

#Q Write a function, sublist, that takes in a list of strings as the parameter. In the function, use a while loop to return a sublist of the input list. The sublist should contain the same values of the original list up until it reaches the string “STOP” (it should not contain the string “STOP”).

def sublist(stri1):
    lsit3=[]
    number=0
    while number<len(stri1):
        if stri1[number]=='STOP':
            break
        else:
            lsit3.append(stri1[number])
            number = number+1
    return lsit3
            
str1=['apple','bana','ali','hassan','STOP']    
sublist(str1)   
    
#QWrite a function called stop_at_z that iterates through a list of strings. Using a while loop, append each string to a new list until the string that appears is “z”. The function should return the new list.  
 
def stop_at_z(stri1):
    lsit3=[]
    number=0
    while number<len(stri1):
        if stri1[number]=='Z':
            break
        else:
            lsit3.append(stri1[number])
            number = number+1
    return lsit3

s1=['apple','bana','ali','hassan','STOP','Z','a','b']
stop_at_z(s1)   
    
#Q Below is a for loop that works. Underneath the for loop, rewrite the problem so that it does the same thing, but using a while loop instead of a for loop. Assign the accumulated total in the while loop code to the variable sum2. Once complete, sum2 should equal sum1.

sum1 = 0

lst = [65, 78, 21, 33]

for x in lst:
    sum1 = sum1 + x
  
print(sum1)
    
numer1=0  
sum2=0 
while numer1<len(lst):
    sum2=sum2+lst[numer1]
    numer1=numer1+1
print(sum2)

'''  
#Q Write a function called beginning that takes a list as input and contains a 
while loop that only stops once the element of the list is the string ‘bye’.
 What is returned is a list that contains up to the first 10 strings, 
 regardless of where the loop stops. 
 (i.e., if it stops on the 32nd element, the first 10 are returned. 
  If “bye” is the 5th element, the first 4 are returned.) 
 If you want to make this even more of a challenge, do this without slicing


'''

def beginning(s2):
    s3=s2
    emp_list=[]
    num=0
    num2=0
    if len(s2)>10:
            while num2!=10:
                if s3[num2]=='bye':
                    break 
                else:
                   emp_list.append(s3[num2])
                   num2=num2+1  
    else:
        while num<len(s2):
                if s3[num]=='bye':
                    break
                else:
                    emp_list.append(s3[num])
                    num=num+1
             
    return emp_list
    

s1=['apple','bana','ali','hassan','STOP','Z','b','b','b','b','b','b','b','b','b','b','b','b','b','bye','b','b','b',]

beginning(s1)
        
        
        
        
                    
            
            
            
            
            
            
            
            
            
            
            
        
        
        
        
        
        num=num+1
        
    













   









    
    