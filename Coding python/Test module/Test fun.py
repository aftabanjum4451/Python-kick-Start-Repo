# -*- coding: utf-8 -*-
"""
Created on Sat Sep 12 09:31:59 2020

@author: aftab
"""


def distance(x1, y1, x2, y2):
    return 0
import test
#test.testEqual(distance(1, 2, 1, 2),0)
#test.testEqual(distance(1,2, 4,6),5)
#test.testEqual(distance(0,0, 1,1),2**0.5)



class Point:
    """ Point class for representing and manipulating x,y coordinates. """

    def __init__(self, initX, initY):

        self.x = initX
        self.y = initY

    def distanceFromOrigin(self):
        return ((self.x ** 2) + (self.y ** 2)) ** 0.5

    def move(self, dx, dy):
        self.x = self.x + dx
        self.y = self.y + dy


#testing class constructor (__init__ method)
p = Point(3, 4)

print( p.y == 4)
print( p.x == 3)

#testing the distance method
p = Point(3, 4)
print(p.distanceFromOrigin() == 5.0)

#testing the move method
p = Point(3, 4)
p.move(-2, 3)
print(p.x == 1)
print(p.y == 7)
