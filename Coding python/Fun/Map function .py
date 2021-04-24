# -*- coding: utf-8 -*-

abbrevs = ["usa", "esp", "chn", "jpn", "mex", "can", "rus", "rsa", "jam"]

def upcase1(st):
    return st.upper()

trans=list(map(upcase1,abbrevs))
print(trans)

#2ns method by lambda expression 

trans=list(map(lambda st: st.upper(),abbrevs))
print(trans)

# make upper case letter only first two letter and return these two uper case letter

def upcase1(st):
    return st[0:2].upper()

trans=list(map(upcase1,abbrevs))
print(trans)

# return first two letter uppercase and rest the same 

def upcase_lter(st):
    a=st[0:2].upper()
    b=st[2:]
    return a+b

trans=list(map(upcase_lter,abbrevs))
print(trans)

'''
# Q Using map, create a list assigned to the variable greeting_doubled 
that doubles each element in the list lst.
'''
lst = [["hi", "bye"], "hello", "goodbye", [9, 2], 4]

def double_value(st):
    return 2*st

greeting_doubled=list(map(double_value,lst))
print(trans)




    






