# -*- coding: utf-8 -*-
"""
Created on Mon Aug 24 09:59:15 2020

@author: aftab
"""


import json 
#dumps function 
# a Python object (dict):
x = {
  "name": "John",
  "age": 30,
  "city": "New York"
}

# convert into JSON:
y = json.dumps(x)# its conver what ever given to its as parameter to string

# the result is a JSON string:
print(type(y))

#loads method 
# always pass sting and if the string contain dic it will conver into dic andif list conver into list 
a_string = '\n\n\n{\n "resultCount":25,\n "results": [\n{"wrapperType":"track", "kind":"podcast", "collectionId":10892}]}'
y1 = json.loads(a_string)
print(y1['resultCount'])
print(json.dumps(42))







