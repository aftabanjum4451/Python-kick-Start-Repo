# -*- coding: utf-8 -*-
"""
Created on Tue Jun  2 14:31:14 2020

@author: aftab
"""
# all string method and attribute
#\'	Single Quote	
#\\	Backslash	
#\n	New Line
#Note: All string methods returns new values. They do not change the original string.

s='hello pakistan'
s='''i love pakistna 
i am curently in china
i love the moutain''' # in order to creat multile line string 
print(s)
print(s[0])

#string silicing 
print(s[0:5])
print(s[0:-1])

#accesing  last item of sting 
print(s[-1])
print(len(s))
print(s[len(s)-2])

# strip methos: to remove white spaces from the start and begning of the string 
s1='  hello lahore  '
print(len(s1))
print(s1.strip())
print(len(s1.strip()))

# lower method(): to convert string into lowe cases letter
S2='I LOVE Being in LAB '
print(S2.lower())

#upper method(): to convert string into upper case letter 
S2='I LOVE Being in LAB '
print(S2.upper())

#replace method() we can replace any letter or whole word by using replace function 
# we need to pass two parameter to replace funtion, first parameter will be the lcation and 2nd the thing that we need to add
S3='hi i am stuck at work i guess i cant make it'
print(S3.replace('hi','good bye'))
print(S3.replace(S3[0:5],'good bye'))
print(S3.replace(S3[0],'1253'))

#Split() stplit the string according to the delimeter specific in the string 
#NOTE: split function return a list
S4='hi where you going, i want to talk to you about your homework, so come back right now '
result=S4.split(' ')
print(result)
print(type(result))
print(S4.split(' '))
print(type(S4))

#checking method(): check if the letter or string present in the string or not 
S5='hi would you like to go out with me '
x='out'in S5 # for in method 
print(x)

x1='pakistan'not in  S5 # for not in method
print(x1)

#String Concatenation
a='hello'
b='pakistani'
c='in lahore'
print(c[-5:-2])
print(a+b+c)
print(a+' '+b+' '+c)
print(a[0:1]+b[0:-1]+c[-5:-2])
a1='12'
d=a+b+ a1 +c
print(d)

#String Format method : inorder to concatenate string and other datatype

name='aftab'
country='pakistan'
age=35
print(name+' ',country)# error cant add string and int
text=name+' ',country,{}# this type of style conver it into tuple 
text=str(text)# inorder to apply format function need to convert into string
print(text)
print(text.format(age))
print(text)
#example 2
quantity = 3
itemno = 567
price = 49.95
myorder = "I want {} pieces of item {} for {} dollars."
print(myorder.format(quantity, itemno, price))

#exapmle 3
age=35
name='aftab'
country='pakistan'
language='urdue'
job='teacher'
salary=45000
text1='i am {}. i am from {}. i am {} year old. i speak {}. i am a {} and my salary is {}'
print(type(text1))
print(text1.format(name,country,age,language,job,salary))

#Escape Character: inorder to add string at any point in the string
#txt = "We are the so-called "Vikings" from the north."# give error if we do insert
tet = "We are the so-called  \"Vikings \" from the north."
print(tet)

#String endswith() Method: to find where the string ends
S6='hi my brother is not feeling well today.'
print(S6.endswith('.'))
print(S6.endswith('today'))
print(S6.endswith('today.',-1,-2))
print(S6.endswith('my',3,5))# can check at specific index strin end with
print(S6.endswith('my brother is not feeling well today',3,-1))

#count method():to count specific srting or letter in the string

S7='hi, hiw are you?,123,how you feeling today'
print(S7.count('you'))
print(S7.count('i',1,10))# count from given start index and from given end index 

#String find() Method: to find string or letter in the string and given index value
S8='hi, hiw are you?,123,how[you] feeling [today]'
print(S8.find('2'))
print(S8.find('['))
print(S8.find('2'))
print(S8.index('2'))#same as find function
print(S8[18])

#String index(): return index value
S9='hi, hiw are you?,123,how you feeling today'
print(S9.index('i'))
print(S9.index('h',0,-1))

#String isalnum(): Check if all the characters in the text are alphanumeric
S10='hi, hiw are you?,123,how you feeling today'
S11='123'
print(S11.isalnum())
print(S10.isalnum())

#String isalpha(): Check if all the characters in the text are letters:
S12='hi, how are you how you feeling today'
S13='hello'
print(S12.isalpha())
print(S13.isalpha())

#String isdigit() :Check if all the characters in the text are digits:
txt = "50800"
x = txt.isdigit()
print(x)

#String join() :Join all items in a tuple into a string, using a hash character as separator:
myTuple = ("John", "Peter", "Vicky")
x = "#".join(myTuple)
print(x)

myDict = {"name": "John", "country": "Norway"}
mySeparator = "TEST"
x = mySeparator.join(myDict)
print(x)

#String rsplit():Split a string into a list, using comma, followed by a space (, ) as the separator:
S12='hi i am aftab, and i am a master student, at  unuversity of jinan china shandong'
print(S12.rsplit(','))
#2nd example 
txt = "apple, banana, cherry"
x = txt.rsplit(", ")
print(x)

#3rd example
txt = "apple, banana, cherry"
# setting the maxsplit parameter to 1, will return a list with 2 elements!
x = txt.rsplit(", ", 3)# 3 determine how many element in the list would be 
print(x)

#String rstrip() :to remove  spaces from the right
S14='   hi jack how are you.   '
print(len(S14))
print(len(S14.rstrip()))
#2nd exapmle
txt = "banana,,,,,ssaaww....."
x = txt.rstrip(".was")
print(x)

txt = "banana,,,,,ssaaww....."
x = txt.rstrip(".aws")
print(x)

txt = "banana,,,,,ssaaww....."
x = txt.rstrip(",.was")
print(x)

#String splitlines():Split a string into a list where each line is a list item:
txt = "Thank you for the music\nWelcome to the jungle"
x = txt.splitlines()
print(x)
print(x[0])

#startswith():Check if the string starts with "Hello":
txt = "Hello, welcome to my world."

x = txt.startswith("Hello")

print(x)

#2 example
txt = "Hello, welcome to my world."
x = txt.startswith("wel", 7, 20)
print(x)


#String zfill():Fill the string with zeros until it is 10 characters long:
txt = "50"
x = txt.zfill(10)
print(x)

#2nd example
a = "hello"
b = "welcome to the jungle"
c = "10.000"
print(a.zfill(10))
print(b.zfill(10))
print(c.zfill(10))

#formateed string 
name='hassan'
age=15
print(f'you name is {name} and you are {age} years old ')

#back string reading 
s='123456789'
print(s[::-1])

