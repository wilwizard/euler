from __future__ import division
from sys import argv
import funcs

script, num = argv
limit = int(num)
array = []

for x in range(2,limit):
	total=0
	for y in list(str(x)):
		y = int(y)
		total+=y**5
	if(total==x):
		print x
		array.append(x)
print '======='
print sum(array)

		

	