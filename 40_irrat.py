from __future__ import division
from sys import argv
import funcs

script, limit = argv
limit=int(limit)

array=[int(x) for x in list(''.join([str(x) for x in range(limit)]))]
print array[1]*array[10]*array[100]*array[1000]*array[10000]*array[100000]*array[1000000]