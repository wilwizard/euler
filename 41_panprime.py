from __future__ import division
from sys import argv
import funcs
import itertools 

script, limit = argv
limit=int(limit)+1

for n in [list(x) for x in list(itertools.permutations('7654321',7))]:
    if funcs.is_prime(int(''.join(n))):
        print int(''.join(n))
        break 