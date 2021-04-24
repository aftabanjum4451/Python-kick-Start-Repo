# -*- coding: utf-8 -*-
"""
Created on Mon Aug 24 08:08:20 2020

@author: aftab
"""
#nested list
nestlist1=[1,2,3,4,['ali','lahore','pakistan'],['willian',24.7,8.5]]
print(nestlist1[4])
print(nestlist1[4][0])
print(nestlist1[5][0])
nestlist1[4].append('hassan')
print(nestlist1)


nestedlist2=[[1,2,3,4,5],['ali','lahore'],{7:'ali',77: 'aliali'}]

print(nestedlist2[2][7])

#nested dictionary 
dic1={'communication':{'mobile':{'apple':2400,'samsung':2500,'laptop':{'acces':10000,'dell':20000,'minilaptop':{'mini apple':150000,'mini dell':240000}}}}
      
      }

dic1['communication']['mobile']['laptop']['minilaptop']['mini apple']='too expanesive'

print(dic1['communication']['mobile']['laptop']['minilaptop']['mini apple'])
     

#Q Below, we have provided a list of lists that contain information about people. Write code to create a new list that contains every person’s last name, and save that list as last_names.

info = [['Tina', 'Turner', 1939, 'singer'], ['Matt', 'Damon', 1970, 'actor'], ['Kristen', 'Wiig', 1973, 'comedian'], ['Michael', 'Phelps', 1985, 'swimmer'], ['Barack', 'Obama', 1961, 'president']]

def lastname(lsit):
    info=lsit
    last_names=[]
    for item in info:
        last_names.append(item[1])
    return last_names       
    
        
lastname(info)    
          
#Q Below, we have provided a list of lists named L. Use nested iteration to save every string containing “b” into a new list named b_strings.            
 
L = [['apples', 'bananas', 'oranges', 'blueberries', 'lemons'], ['carrots', 'peas', 'cucumbers', 'green beans'], ['root beer', 'smoothies', 'cranberry juice']]

b_strings=[]

for item in L:
    for itemin in item :
        if 'b'in itemin:
          b_strings.append(itemin)  
   
print(b_strings)
    

#
'''
Below, we have provided a nested list called big_list. 
Use nested iteration to create a dictionary, word_counts, 
that contains all the words in big_list as keys, 
and the number of times they occur as values.
'''
big_list = [[['one', 'two'], ['seven', 'eight']], [['nine', 'four'], ['three', 'one']], [['two', 'eight'], ['seven', 'four']], [['five', 'one'], ['four', 'two']], [['six', 'eight'], ['two', 'seven']], [['three', 'five'], ['one', 'six']], [['nine', 'eight'], ['five', 'four']], [['six', 'three'], ['four', 'seven']]]

d={}
count=0
for item in big_list:
    #print(item)
    for valu_initen in item:
        #print(valu_initen)
        for secnd_value in valu_initen:
            if secnd_value in d:
                d[secnd_value]=d[secnd_value]+1
            else:
                d[secnd_value]=1
print(d)
    

'''
Iterate through the list so that if the character ‘m’ is in the string, 
then it should be added to a new list called m_list. Hint: Because this 
isn’t just a list of lists, think about what type of object you want
 your data to be stored in. Conditionals may help you.


'''
d = ['good morning', 'hello', 'chair', 'python', ['music', 'flowers', 'facebook', 'instagram', 'snapchat', ['On my Own', 'monster', 'Words dont come so easily', 'lead me right']], 'Stressed Out', 'Pauver Coeur', 'Reach for Tomorrow', 'mariners song', 'Wonder sleeps here']

m_list=[]
for il1 in d:
    if type(il1)!=list and 'm' in il1:
        m_list.append(il1)
    if type(il1) is list:
        for il2 in il1:
            if type(il2)!=list and 'm' in il2:
                m_list.append(il2)
            if type(il2) is list:
                for il3 in il2:
                    if 'm' in il3:
                      m_list.append(il3)  
                    print(il3)
                
            
print(m_list)        
 
'''
The nested dictionary, pokemon, shows the number of various Pokemon 
that each person has caught while playing Pokemon Go. Find the total
 number of rattatas, dittos, and pidgeys caught and assign to the 
 variables r, d, and p respectively. Do not hardcode. 
 Note: Be aware that not every trainer has caught a ditto.

'''           
pokemon = {'Trainer1':
          {'normal': {'rattatas':15, 'eevees': 2, 'ditto':1}, 'water': {'magikarps':3}, 'flying': {'zubats':8, 'pidgey': 12}},
        
          'Trainer2':
          {'normal': {'rattatas':25, 'eevees': 1}, 'water': {'magikarps':7}, 'flying': {'zubats':3, 'pidgey': 15}},
          'Trainer3':
          {'normal': {'rattatas':10, 'eevees': 3, 'ditto':2}, 'water': {'magikarps':2}, 'flying': {'zubats':3, 'pidgey': 20}},
          'Trainer4':
          {'normal': {'rattatas':17, 'eevees': 1}, 'water': {'magikarps':9}, 'flying': {'zubats':12, 'pidgey': 14}}}
                
            

 
r=0
d=0
p=0  
for item in pokemon.keys():
    for item2 in pokemon[item] :
        for item3 in pokemon[item][item2]:
            if item3=='rattatas':
                r=r+pokemon[item][item2][item3]
            if item3=='ditto':
                d=d+pokemon[item][item2][item3]
            if item3=='pidgey':
                p=p+pokemon[item][item2][item3]
                
print(r,d,p)                
                
            
        

 
   
    
    
 
    
    
    
    
            
        
        
    
    









      
  