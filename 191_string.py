from __future__ import division
from sys import argv
import funcs
import re

script, number = argv
num = int(number)
tally=0

def loa(num):
	ret_array = []
	if num==1:
		return ['L','O','A']
	else:
		for x in loa(num-1):
			ret_array.append(x+'L')
			ret_array.append(x+'O')
			ret_array.append(x+'A')
		return ret_array

for x in loa(num):
	check=True
	regex = re.compile('AAA')
	if regex.search(x):
		check=False
	if list(x).count('L')>1:
		check=False
	if check:
		print x
		tally+=1
print '======'
print tally