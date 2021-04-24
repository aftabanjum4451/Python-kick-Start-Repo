# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

def unique_list(l):
  x = []
  for a in l:
    if a not in x:
      x.append(a)
  return x

print(unique_list([1,2,3,3,3,3,4,5])) 


def pascal_triangle(n):
   trow = [1]
   y = [0]
   for x in range(max(n,0)):
      print(trow)
      trow=[l+r for l,r in zip(trow+y, y+trow)]
   return n>=1
pascal_triangle(6) 


def reverse_word(string):
    return ' '.join(string.split(' ')[::-1])
    
print(reverse_word(input('Please input a sentence:')))


def generate_passwords(level):
    import string
    import random
    
    level_dict = {'low':8, 'middle':12, 'high':16}
    
    segment = [0, 0, 0, 0]
    for x in range(level_dict[level]):
        r = random.randint(0,3)
        segment[r] += 1
    
    lower_letter = random.choices(string.ascii_lowercase, k=segment[0])
    upper_letter = random.choices(string.ascii_uppercase, k=segment[1])
    digits = random.choices(string.digits, k=segment[2])
    symbols = random.choices('!@#$%^&*()_+', k=segment[3])
    
    password = lower_letter + upper_letter + digits + symbols
    random.shuffle(password)
    
    return ''.join(password)

def check_level_input(string, level):
   
    if string.lower() == level or string.lower() == level.lower()[0]:
        return True
    else:
        return False
    
def main():
    while True:
        level = input('Choose your password security level: [low/middle/high]')
        if level.lower() == 'exit':
            break
        elif check_level_input(level, 'low'):
            print(generate_passwords('low'))
        elif check_level_input(level, 'middle'):
            print(generate_passwords('middle'))
        elif check_level_input(level, 'high'):
            print(generate_passwords('high'))
        else:
            print('Input error.')
        
if __name__ == "__main__":
    main()

