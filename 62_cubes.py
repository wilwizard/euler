from __future__ import division
from sys import argv
import funcs
import itertools


cubes=[]
array2=[]
for x in range(1000):
    cubes.append(x**3)
    
for c in cubes:
    carray=list(str(c))
    carray.sort()
    array2.append(int(''.join(carray)))

array2.sort()


prev=-1
freq={}
for a in array2:
    if a!=prev:
        freq[a]=1
    elif a==prev:
        freq[a]+=1
    
    prev=a
    
for a in array2:
    if freq[a]>4:
        print a