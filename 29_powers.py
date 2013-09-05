from __future__ import division
from sys import argv
import funcs

script, num = argv
limit = int(num)
array = []

for a in range(2,limit+1):
	for b in range(2,limit+1):
		array.append(a**b)
		
print len(list(set(array)))


	