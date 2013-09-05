from __future__ import division
from sys import argv
import funcs
import math
import fractions

script, limit = argv
limit=int(limit)

def cycleLen(d):
    if d == 1:
        return 0
    if d % 2 == 0:
        return cycleLen(d / 2)
    elif d % 5 == 0:
        return cycleLen(d / 5)
    else:
        cnt = 1
        while int('9' * cnt) % d != 0:
            cnt += 1
        return cnt

max = 0
d = -1
for i in range(2, limit):
    l = cycleLen(i)
    if l > max:
        max = l
        d = i
        print d,max

        

    

    
    