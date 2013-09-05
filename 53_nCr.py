from __future__ import division
from sys import argv
import funcs

script, limit = argv
limit = int(limit)

count=0
for n in range(100,22,-1):
    r=1
    while funcs.nCr(n,r)<limit:
        r+=1
    count+=(n-2*r+1)
    print n,r
print count