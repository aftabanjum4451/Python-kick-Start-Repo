# -*- coding: utf-8 -*-
"""
Created on Wed Jun  3 18:19:30 2020

@author: aftab
"""
#Accumulator pattrent 
list1=[1,2,4,5,6,7,8,9,10,15]
w=0
for i in list1:
    w=w+i
print(w)
  
#Count the number of characters in string str1. Do not use len(). Save the number in variable numbs.
str1 = "I like nonsense, it wakes up the brain cells. Fantasy is a necessary ingredient in living."
w=0
for i in str1:
    w+=1
    print(w)
numbs=w

#question 2
'''
Create a list of numbers 0 through 40 and assign this list to the variable numbers.
Then, accumulate the total of the list’s values and assign that sum to the variable sum1.

'''
my_list=[]
for i in range(0,41):
    my_list.append(i)
print(my_list) 
numbers=my_list
print(numbers)
w=0
for i in numbers:
    w=w+i
sum1=w
print(sum1)

#question 
s = "python"
for idx in range(len(s)):
   print(s[idx % 2])
   
#
my_str = "MICHIGAN"
for i in my_str:
    print(i)
    
'''
Write one for loop to print out each element of the list several_things.
Then, write another for loop to print out the TYPE of each element of the list several_things. 
To complete this problem you should have written two different for loops, 
each of which iterates over the list several_things, 
but each of those 2 for loops should have a different result.

'''  

several_things = ["hello", 2, 4, 6.0, 7.5, 234352354, "the end", "", 99]

for i in several_things:
    print(i)
for k in several_things:
    print(type(k))
  
#question 
'''
Write code that uses iteration to print out 
the length of each element of 
the list stored in str_list 
'''   
str_list = ["hello", "", "goodbye", "wonderful", "I love Python"]

for i in str_list:
    print(len(i))


#question 
'''
Write code to count the number of characters in original_str using the accumulation pattern and assign the answer to a variable num_chars. 
Do NOT use the len function to solve the problem (if you use it while you are working on this problem, comment it out afterward!)
'''

original_str = "The quick brown rhino jumped over the extremely lazy fox."

w=0
for i in original_str:
    print(i)
    w=w+1
print(w)
num_chars=w
    
#question

'''
addition_str is a string with a list of numbers separated by the + sign. 
Write code that uses the accumulation pattern to take the sum of all of the numbers and assigns it to sum_val (an integer).
 (You should use the .split("+") function to split by "+" and int() to cast to an integer).
'''
addition_str = "2+5+10+20"
result1=addition_str.split('+')
w=0
for i in result1:
    i=int(i)
    w=w+i
sum_val=w
print(sum_val)    


#question 
'''
week_temps_f is a string with a list of fahrenheit temperatures separated by the , sign. 
Write code that uses the accumulation pattern to compute the average (sum divided by number of items) and assigns it to avg_temp. 
Do not hard code your answer (i.e., make your code compute both the sum or the number of items in week_temps_f) 
(You should use the .split(",") function to split by "," and float() to cast to a float).
'''
week_temps_f = "75.1,77.7,83.2,82.5,81.0,79.5,85.7"
answer=week_temps_f.split(',')
print(answer)
w=0
for i in answer:
    i=float(i)
    w=w+i
avg_temp=w/len(answer)
print(avg_temp)


#question
'''
Write code to create a list of numbers from 0 to 67 and assign that list to the variable nums. 
Do not hard code the list.
'''
nums=[]
for i in range(0,68):
    nums.append(i)
print(nums)


#question 
'''
Write code to create a list of word lengths for the words in original_str 
using the accumulation pattern and assign the answer to a variable num_words_list. 
(You should use the len function).
'''
    
original_str = "The quick brown rhino jumped over the extremely lazy fox"
result=original_str.split(' ')
print(result)
num_words_list=[]
for i in result:
    num_words_list.append(len(i))
print(num_words_list)


#question 
'''
Create an empty string and assign it to the variable lett. 
Then using range, write code such that when your code is run, 
lett has 7 b’s ("bbbbbbb").
'''
print(len("bbbbbbb"))

my_list=[]
lett=my_list
str102=''
for i in range(0,7):
    str102=str102+'b'
    
lett=str102
print(lett)

#question 
'''
Write a program that uses the turtle module and a for loop to draw something. 
It doesn’t have to be complicated, but draw something different than we have done in the past. 
(Hint: if you are drawing something complicated, it could get tedious to watch it draw over and over. 
Try setting .speed(10) for the turtle to draw fast, or .speed(0) for it to draw super fast with no animation.)
'''



















