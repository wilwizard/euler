from __future__ import division
from sys import argv
import funcs

script, limit = argv
limit = int(limit)

ms=0
for a in range(1,limit):
    for b in range(1,limit):
        ms=max(ms,sum(funcs.num_to_array(a**b)))
        
        
print ms