from __future__ import division
from sys import argv
import funcs

script, limit = argv
limit=int(limit)+1
#file = open('file.txt','w')

total=0
for x in range(1,limit):
    total+=x**x
print str(total)[-10:]