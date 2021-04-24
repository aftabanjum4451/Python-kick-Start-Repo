# -*- coding: utf-8 -*-
"""
Created on Fri Jun  5 15:49:30 2020

@author: aftab
"""
#Q1 Could aliasing cause potential confusion in this problem?
b = ['q', 'u', 'i']
z = b
b[1] = 'i'
z.remove('i')
print(z)

#Q2 Could aliasing cause potential confusion in this problem?
sent = "Holidays can be a fun time when you have good company!"
phrase = sent
phrase = phrase + " Holidays can also be fun on your own!"

print(sent)

#Q5
sent = "The mall has excellent sales right now."
wrds = sent.split()
wrds[1] = 'store'
new_sent = " ".join(wrds)
print(new_sent)