from __future__ import division
from sys import argv
import funcs

script, number = argv
limit = int(number)
total=0

for x in xrange(limit):
	if funcs.is_prime(x):
		print x
		total+=x
print '======'
print total