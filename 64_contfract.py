from __future__ import division
from sys import argv
import funcs
import math
import fractions

script, limit = argv
limit=int(limit)
file = open('file.txt','w')
  
    
def reps(n):
    s=math.sqrt(n)
    a1,a0=math.modf(s)
    x=0
    seq=[]

        x=(1/a1)%1.0
        seq.append(int(1/a1))
    

    
    