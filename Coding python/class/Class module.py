# -*- coding: utf-8 -*-
# simple class creation 

class pointer():
    def getx(self):
        return self.x
        
point1=pointer()
point2=pointer()

point1.x=5
point2.x=10

print(point1.getx())
print(point2.getx())

# class creation and variable intilization 

class student():
    def __init__(self):
        self.name='ali'
        self.age=30
        self.city='lahore'
        self.university_name='UOL'
    def get_name(self):
        return self.name
    
student1=student()

print(student1.university_name)

print(student1.get_name('hamza')) 


#2nd example
class student_lahore():
    def __init__(self,name,age,city,university_name):
        self.name=name
        self.age=age
        self.city=city
        self.university_name=university_name
    def get_name(self):
        return self.name
    
student1=student_lahore('john hunry',32,'lahore','UOL')

print(student1.age)

print(student1.university_name)

print(student1.get_name())




# 3rd example
class Point:
   
    def __init__(self):

        self.x = 0
        self.y = 0

p = Point()        
q = Point()         

print(p)
print(q)

print(p is q)

# constructor to intilized the object instances
class point():
    def __init__(self,x,y):
        self.x=x
        self.y=y
           
point1=point(2,5)
point2=point(10,25)
print(point1.x)
print(point1.y)    
print(point2.x)


# animal class example

class animal():
    def __init__(self,arms, legs):
        self.arms=arms
        self.legs=legs
    def limbs(self):
        return self.arms+self.legs

spider=animal(4,4)

spidlimbs=spider.limbs()
print(spidlimbs)

# string  conversion  

class Cereal ():
    def __init__(self,n,b,f):
        self.name=n
        self.brand=b
        self.fiber=f
    def __str__(self):
        return '{} cereal is produced by {} and has {} grams of fiber in every serving!'.format(self.name, self.brand, self.fiber)                   
    
               
c1=Cereal('Corn Flakes',"Kellogg's",2 ) 
print(c1)
c2=Cereal("Honey Nut Cheerios","General Mills",3)  
print(c2)



class add_number():
    def __init__(self,x,y):
        self.x=x
        self.y=y
        
    def getx(self):
        return self.x
    def gety(self):
        return self.y
    
    def modifx(self,num):# modified the value of x by mathod inside of cass
        self.x=num
        return self.x
    def __str__(self):
        return 'number1 is {} and number2 is {}'.format(self.x,self.y)
    def __add__(self, secnumber):
        return self.x+secnumber.x,self.y+secnumber.y
    def __sub__(self, secnumber):
        return self.x-secnumber.x,self.y-secnumber.y
    
    
        
ab=add_number(3,4)
ac=add_number(3,4)
print(ab.modifx(25))

print(ab)
print(ab+ac)
print(ab-ac)

        
# sorting function by using class method 



class fruit ():
    def __init__(self,name,price):
        self.name=name
        self.price=price
    def sorted_price(self):
        return self.price
    
d=[
   fruit('apple',100),
   fruit('orange',50),
   fruit('banana',60),
   fruit('cherry',25)
   ]
     
result=sorted(d, key=fruit.sorted_price) 
print(result)
for item in result:
    print(item.name)
    
    
 # ghraph representation 
class Point:
    """ Point class for representing and manipulating x,y coordinates. """

    printed_rep = "*"

    def __init__(self, initX, initY):

        self.x = initX
        self.y = initY

    def graph(self):
        rows = []
        size = max(int(self.x), int(self.y)) + 2
        #print('the value of size is  ',size)
        for j in range(size-1) :
            if (j+1) == int(self.y):
                special_row = str((j+1) % 10) + (" "*(int(self.x) -1)) + self.printed_rep
                #print('the special row is ',special_row)
                rows.append(special_row)
            else:
                rows.append(str((j+1) % 10))
        rows.reverse()  # put higher values of y first
        x_axis = ""
        for i in range(size):
            x_axis += str(i % 10)
        rows.append(x_axis)
        print('the row is ',  rows)

        return "\n".join(rows)


p1 = Point(2, 3)
p2 = Point(3, 12)
print(p1.graph())
print()
print(p2.graph())



   
    
       
        
        
        
        
        
    
    
    













        
        
        
        
        
        
        
    



































    










  
    
    
        
        












    
    
    
    
    
    
    
    
    
    
    
    

