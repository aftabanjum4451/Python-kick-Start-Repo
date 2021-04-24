# -*- coding: utf-8 -*-

#.................dictionaries .................

#dictionary creation 
my_dic={}
my_dic={'one':124,'two':2547}
print(my_dic)
print(my_dic['one'])

my_dic2={}
my_dic2['1']=4254
my_dic2['2']=8975
my_dic2['three']=10.355

my_dic2[1]=4254
my_dic2[2]=8975
my_dic2[3]=10.355
print(my_dic2)
#for loop for getting value from dic
for item in my_dic2:
    print(my_dic2[item])
    
'''...........dictionary operator............'''
#update value
dic_1={'one':2547, 'two': 78745, 'three':7845}
dic_1['three']=0
print(dic_1)
dic_1={'one':2547, 'two': 78745, 'three':7845}
dic_1['three']=dic_1['one']*2547
print(dic_1)
dic_1['two']=dic_1['one']+dic_1['three']
print(dic_1)
swimmers = {'Manuel':4, 'Lochte':12, 'Adrian':7, 'Ledecky':5, 'Dirado':4, 'Phelps':23}
print(swimmers)
swimmers['Phelps']=swimmers['Phelps']+5
print(swimmers)
print(len(swimmers))

#del function
del swimmers ['Lochte']
print(swimmers)
#del()
del swimmers # delet whole dictionary
inventory = {'apples': 430, 'bananas': 312, 'oranges': 525, 'pears': 217}
for key in inventory.keys():
    print(key)

for key in inventory.keys():
    print(inventory[key])
my_temp_dic=list(inventory.keys()) #give list of value key but remember not in order
print(my_temp_dic)

my_temp_dic=list(inventory.values()) #give list of key values but remember not in order
print(my_temp_dic)

for x in inventory.values():
  print(x)

#items 
my_temp_dic=list(inventory.items()) #give tuple of key and its values 
print(my_temp_dic)

for item in my_temp_dic:
    print(item)

    
for x,y in inventory.items() :
    print(x, y)

#in()
inventory = {'apples': 430, 'bananas': 312, 'oranges': 525, 'pears': 217}

print('apples'in inventory ) # return boolen value
print('cat'in inventory) # return boolen value   
    
if 'apples' in inventory:
    print('yes apple in inventory',inventory['apples'] )
else:
    print('no there is no apple in the inventory')
    
#get()

print(inventory.get("apples"))
print(inventory.get("cherries"))

print(inventory.get("cherries",None))# Optional. A value to return if the specified key does not exist Default value None

for key in inventory:
    print(inventory.get(key))
  
# pop ()
inventory = {'apples': 430, 'bananas': 312, 'oranges': 525, 'pears': 217}
print(inventory.pop('oranges'))
print(inventory)
inventory = {'apples': 430, 'bananas': 312, 'oranges': 525, 'pears': 217}
print(inventory.popitem())
print(inventory)
#clear()
inventory = {'apples': 430, 'bananas': 312, 'oranges': 525, 'pears': 217}
inventory.clear()
print(inventory)
#copy()
inventory = {'apples': 430, 'bananas': 312, 'oranges': 525, 'pears': 217}
my_fr=inventory.copy()
print(my_fr)

#nested dic
myfamily = {
  "child1" : {
    "name" : "Emil",
    "year" : 2004
  },
  "child2" : {
    "name" : "Tobias",
    "year" : 2007
  },
  "child3" : {
    "name" : "Linus",
    "year" : 2011
  }
}
  
print(myfamily["child1"]['name'])

my_nested_dic={
        
        'my_f_dic1':{
                'name':'ali',
                'age':25,
                'city':'lahore'
                },
      'my_dic2':{
             'name':'hassan',
             'age':45,
             'country': 'pakistan'
              
              }  
  
        }
      
for key in my_nested_dic.items():
    print(key)
    
print(my_nested_dic)

# fromkeys() 
x = ('key1', 'key2', 'key3', 'key4')
y = 25
thisdict = dict.fromkeys(x, y)
print(thisdict)

#setdefault()
car = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}

x = car.setdefault("color", "white")

print(x)
print(car)
car = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}

x = car.setdefault("model", "Bronco")# return key value if key is present in dic 

print(x)
print(car)

#update()
car = {
    "year": 1964,
  "brand": "Ford",
  "model": "Mustang"
  
}
car.update({"color": "White"})
print(car)
# enumerate()
for i, v in enumerate(car):
 print(i, v)
#in function to check if the key is present in dic 

my_dict = {"username": "XYZ", "email": "xyz@gmail.com", "location":"Mumbai"}
print("email" in my_dict)
















































