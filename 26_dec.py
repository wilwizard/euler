from __future__ import division
from sys import argv
import funcs
import math
import fractions

script, limit = argv
limit=int(limit)
file = open('file.txt','w')

max=0
  

def rem(n,d):
    count=0
    while n<d:
        n*=10
        count+=1
    return count,n%d
    
def reps(d):
    count=[]
    a=1
    array=[]
    while not a in array:
        array.append(a)
        c,a=rem(a,d)
        count.append(c)
        if a==0:
            return sum(count)
    return sum(count[array.index(a):])

    
for d in range(2,limit):
    rep=reps(d)
    if reps(d)>max:
        max=rep
        print d,max

        

    

    
    