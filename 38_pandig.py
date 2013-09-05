from __future__ import division
from sys import argv
import funcs

script, limit = argv
limit=int(limit)+1

i=1
maxm=0
#for n in range(1,10):
for d in range(9000,10000): 
    print d
    total=int(''.join([str(d*x) for x in range(1,limit)]))
    if funcs.is_pandig(total,9):
        maxm=max(total,maxm)
print maxm