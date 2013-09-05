from __future__ import division
from sys import argv
import funcs
import itertools


#script,number = argv
x=2
while True:
	if x==funcs.fact_add(x):
		print x
	x+=1