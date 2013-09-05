from __future__ import division
from sys import argv
import funcs

script, number = argv
limit = int(number)

total=0

for x in range(limit):
	temp = funcs.d(x)
	if(funcs.d(temp)==x and x!=temp):
		print '%d:%d' %(x,temp)
		total+=temp
		total+=x
print total/2