# -*- coding: utf-8 -*-
"""
Created on Wed Feb  3 15:22:20 2021

@author: USER
"""

f = open('file1.txt','r')
for line in f:
    print(line)
f.close()

with open ('file1.txt','r') as f :
    for line in f:
        print(line)
    