# -*- coding: utf-8 -*-
"""
Created on Mon Sep  7 15:07:04 2020

@author: aftab
"""

# json.load() function in python 
# its convert the string of list into list #
#or it conver string of dic into dic 
  
import json
x =  '{ "name":"John", "age":30, "city":"New York"}'
z='["123:ali", "2547: 000"]'
y = json.loads(x)
print(type(y))
print(y)




#  dumpand dumps function 
import json 

data={
      
      'user':{
          'name':'ali hassan ',
          'age':30,
          'city': 'lahore'
          
          },
      
      'company':{
          
          'name_company':'lahore limited',
          'location_company':'lahore gulberge',
          'net werth':50000
         
          }
         
      
      }

# dum function its use to write in file 
with open ('data_file.json', 'w') as write_file:
    json.dump(data,write_file, indent=4)

# dumps extract the infomation and conver it into string 
#and return a string 
dumos_vari=json.dumps(data, indent=4)

print(type(dumos_vari))

print(json.dumps(data, indent=4))



# json .dumps() 
# is exteactr the data from the object and conver into the string 

import json
a = {'lalalala': 3}
print(type(a))
myString = json.dumps(a)
print (myString)
print(type(myString))
print(myString[0])


# fecting the data from the url 

import requests
import json

page = requests.get("https://api.datamuse.com/words?rel_rhy=funny")

print(page.text)

print(type(page))
print(page.text[:150]) # print the first 150 characters
print(page.url) # print the url that was fetched
print("------")

x = page.json() # turn page.text into a python object
print(type(x))



# creat url 

import json 
import requests

d={'q':'canada and alberta and night life', 'tbm':'isch'}

reqst=requests.get('https://www.google.com/search',params=d)
print(reqst.url)




















