# -*- coding: utf-8 -*-
"""
Created on Thu Oct 17 15:11:35 2019

@author: leechiyan
"""
import random

# set up variables (y0,x0)
y0=0
x0=0

# random walk one step.
if random.random()<0.5:
    y0=y0+1
else:
    y0=y0-1 

#random x0
if random.random()<0.5:
    x0+= 1
else:
    x0-= 1
print(y0,x0)

# set up variables (y1,x1)
y1=4
x1=3

# random walk one step.
if random.randint(0,99):
    y1=y1+1
else:
    y1=y1-1 

#random x0
if random.randint(0,99):
    x1+= 1
else:
    x1-= 1
print(y1,x1)

# answer = Pythagorian distance between y0,x0 and y1,x1
answer=((y0-y1)**2+(x0-x1)**2)**0.5
print(answer)

# try random.randint(start,end)


