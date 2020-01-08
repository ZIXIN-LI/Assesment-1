# -*- coding: utf-8 -*-
"""
Created on Tue Dec 10 13:31:09 2019

@author: leechiyan
"""
#import matplotlib.pyplot

def get_environment():
    f = open("in.txt")
    environment=[]
    for line in f:
        parsed_line=str.split(line,",")
        rowlist=[]
        for value in parsed_line:
            rowlist.append(float(value))
        environment.append(rowlist)
    print(environment)
    f.close()
    return environment

#matplotlib.pyplot.imshow(environment)
#matplotlib.pyplot.show()    

