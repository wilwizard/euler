from __future__ import division
from sys import argv
import funcs

#script, filename = argv
abfile = open('abnums.txt','w')
file = open('outfile.txt','w')

total = 0
ab_nums = []

print 'calculating abundant numbers'
for x in range(1,28124):
	if sum(funcs.divisors(x))+1>x:
		ab_nums.append(x)
		abfile.write(str(x)+'\n')
print 'Done'
		
for x in range(1,28124):
	can = False
	for a in ab_nums:
		if funcs.in_list(x-a, ab_nums):
			can = True
			break
		if a>x:
			break
	if (not can):
		total+=x
		print x
print '========'
print total