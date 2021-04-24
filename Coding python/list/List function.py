#list creation 
my_list=['123','helle','124225']
print(my_list)

#access item
my_list=['123','helle','124225','pakistan',[1,2,2,4,5],[24,7,'5']]
print(my_list[0])
print(my_list[::])
print(my_list[4][0:2])
print(my_list[4][-1])

#change item 
new_list=[124,45,2,7,8,'ali',1.254,2.57]
new_list[5]=245
print(new_list)
new_list[1:3]=[3,4547.8572,'london']
print(new_list)

#loop through the list
new_list=[124,45,2,7,8,'ali',1.254,2.57]

for i in new_list:
    print(i)
    
#check ifitem exist
new_list=[124,45,2,7,8,'ali',1.254,2.57]   
if 'ali' in new_list:
    print('yes')
    
if 405 in new_list:
    print('yes given item is exist in the list')

#len of the list 
new_list1=[124,254,424,20.14,[24,5,4,77,400],['ali','hassan','hamza'],41,7,8,9]
print(len(new_list1[4]))
print(len(new_list1))

#append function 
new_list2=[12,4,7,8,9]
new_list2.append(24425)
print(new_list2)

#insert functio 
new_list2=[12,4,7,8,9]
new_list2.insert(1,'ali')
print(new_list2)
new_list2.insert(3,'love pakistna')
print(new_list2)

#remove function ()
new_list3=[124,2,4,5,5,['ali','love','pakistan',24,4,5],4.2,5,4]
new_list3[5].remove('ali')
new_list3.remove(124)
print(new_list3)

#pop method()
new_list3=[124,2,4,5,5,['ali','love','pakistan',24,4,5],4.2,5,4]
new_list3.pop()
new_list3.pop(0)
print(new_list3.pop(5))
print(new_list3)

#del keyword
thislist = ["apple", "banana", "cherry"]
del thislist[2]
print(thislist)

#clear method 
thislist = ["apple", "banana", "cherry"]
thislist.clear()
print(thislist)

#copy function 
thislist = ["apple", "banana", "cherry"]
mylist = thislist.copy()
print(mylist)

#join two list
list2 = [1, 2, 3]
list1=[4,5,6]
list3 = list1 + list2
print(list3)

#Append function()
list1 = ["a", "b" , "c"]
list2 = [1, 2, 3]

for x in list2:
    print(x)
    list1.append(x)

print(list1)

#extend function()

list1 = ["a", "b" , "c"]
list2 = [1, 2, 3]

list1.extend(list2)
print(list1)

#sort function 
list2 = [2, 1, 3,4,8,7,9]
list2.sort()
print(list2)

#sorted function 
list2 = [2, 1, 3,4,8,7,9]
print(sorted(list2))
print(list2)

#max function 
list2 = [2, 1, 3]
max(list2)
#min function 
list2 = [2, 1, 3]
min(list2)

#count function 
aList = [123, 'xyz', 'zara', 'abc', 123];
print ("Count for 123 : ", aList.count(123))
print ("Count for zara : ", aList.count('zara'))

#index function 
list1 = ['physics', 'chemistry', 'maths','ali',1,2,3,4,5,6,7,8,9]
print ('Index of chemistry', list1.index(8))
print ('Index of chemistry', list1.index(5,0,-1))

#reverse function 
list1 = ['physics', 'chemistry', 'maths']
list2=[2,3,4,5]
list2.reverse()
print(list2)
list1.reverse()
print(list1)

#sum function 
new_list4=[1,4,7,8,7,25]
sum(new_list4)

#join function 
my_list=['hassan','ali','lahore','school']
sentece=' '
new_list=sentece.join(my_list)
print(new_list)
print(type(new_list))

#list unpacking 
interger_list=[1,2,3]
print(interger_list)
a,b,c=[1,2,3]
print(a)
print(b)
print(c)
interger_list2=[1,2,3,4,5,6,7,8,9,10]
a,b,c, *other,d =[1,2,3,4,5,6,7,8,9,10]
*other,d =[[1,2,3,4,5,6,7,8,9,10],[1,2,3]]
print(a)
print(b)
print(c)
print(other)
print(d)

#Zip function()
#tuple:
a = ("John", "Charles", "Mike")
b = ("Jenny", "Christy", "Monica")
x = zip(a, b)
print(x)
print(*x)
#list:
list1=[2,4,5,4,7,40]
list2=[9,10,11,12,13,25]
result=list(zip(list1,list2))
print(result)
print(type(result))
for item,i in result:
    print(item,i)
result=zip(list1,list2)
print(*result)
#string 
string1='hassan'
string2='lahore'
result=zip(string1,string2)
print(*result)
#parallel 
list1 = [10, 20, 30, 40]
list2 = [100, 200, 300, 400]
result=zip(list1,list2)
print(*result) #can only read eun time 
for x , y in zip(list1,list2):
    print(x,y)

#mutability 
x=[1,2,3,4]
y=x
print(y)
y[0]=254
print(x)
#non mutability  
b='abcd'
a=b
print(a)
print(b)
a='efg'
print(a)
print(b)
print(a in b)

#filter function 
#list
randomList = [1, 'a', 0, False, True, '0']

filteredList = filter(False, randomList)
print(filteredList )
print('The filtered elements are:')
for element in filteredList:
    print(element)
   
#filter function example 
new_list=[1,2,3,4,5,6,7,8,9,10]

def check_evene_number(variable):
    if variable % 2==0:
        return True
    else:
        return False
  
filteredList = filter(check_evene_number, new_list)
print(filteredList )

print('The filtered elements are:')
for element in filteredList:
    print(element)

#3rd example filter method
letters = ['a', 'b', 'd', 'e', 'i', 'j', 'o']
# function that filters vowels
def filterVowels(letter):
    vowels = ['a', 'e', 'i', 'o', 'u']
    if(letter in vowels):
        return True
    else:
        return False
filteredVowels = filter(filterVowels, letters)
print('The filtered vowels are:')
for vowel in filteredVowels:
    print(vowel)






















 
















