from __future__ import division
from sys import argv
import funcs

#script, filename = argv
file = open('number.txt', 'r')
line = ' '
array = []
max_val=0

while line:
	line = file.readline()
	line = line.rstrip()
	array.append(line)
array = map(int,list(''.join(array)))

for x in range(len(array)):
	max_val=max(funcs.prod(array[x:x+5]),max_val)

print max_val
	
