l1=[1,2,3]
l2=[4,5,6]
tuple_l1andl2=list(zip(l1,l2))

for (x1, x2) in tuple_l1andl2:
    print(x1+x2)
    
#list comprehension 
expression=[x1+x2 for(x1, x2 ) in list(zip(l1,l2))]
print(expression)                                          

# without list comprehension and zip
L1 = [1, 5, 2, 16, 32, 3, 54, 8, 100]
L2 = [1, 3, 10, 2, 42, 2, 3, 4, 3]
list_emp=[]

def sum_list(list1,list2):
    for i in range(len(list1)):
        if list1[i]>10 and list2[i]<5:
             result=list1[i]+list2[i]
             list_emp.append(result)
    return list_emp
            
sum_list(L1,L2) 

#with list comprehesnion and zip 

L3= [x1+x2 for (x1, x2) in list(zip(L1,L2)) if x1>10 and x2<5 ]
print(L3)


    










