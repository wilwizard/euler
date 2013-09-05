from __future__ import division
from sys import argv
import funcs

script, filename, iter = argv
file = open(filename, 'w')
iter = int(iter)
array = range(iter)
for x in funcs.iterate(array):
	#print x
	file.write(x+'\n')
