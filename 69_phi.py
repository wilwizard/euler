from __future__ import division
from sys import argv
import funcs
import fractions

script, limit = argv
limit=int(limit)

max_val=0
max_n=0

for n in range(limit,1,-1):
    temp = n/funcs.phi(n)
    if temp > max_val:
        max_n = n
        max_val = temp
    print n,max_n,max_val
    
    
print max_n,max_val