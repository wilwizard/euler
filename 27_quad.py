from __future__ import division
from sys import argv
import funcs

script, num = argv
num = int(num)
cur_max=0
for a in range(-num,num):
	for b in range(-num,num):
		n=0
		while(funcs.is_prime(n*n+a*n+b)):
			n+=1
		if(n>cur_max):
			print n,a,b
			cur_max = n

