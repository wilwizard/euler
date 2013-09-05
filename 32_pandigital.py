from __future__ import division
from sys import argv
import funcs
import itertools



script,limit = argv
file=open('file.txt','w')
prod_set = set([])

num_set=range(1,int(limit)+1)
combs=list(itertools.permutations(num_set))
#print combs

for comb in combs:
	file.write(str(comb)+'\n')
	for mult_pos in xrange(1,len(num_set)-1):
		for eq_pos in xrange(mult_pos+1,len(num_set)):
			mult1=int(''.join(map(str,comb[:mult_pos])))
			mult2=int(''.join(map(str,comb[mult_pos:eq_pos])))
			prod=int(''.join(map(str,comb[eq_pos:])))
			if(mult1*mult2==prod):
				print mult1,'*',mult2,'=',prod
				prod_set.add(prod)
print prod_set
