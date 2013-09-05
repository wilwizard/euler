from __future__ import division
from sys import argv
import funcs

script, number = argv
number = int(number)

# for x in range(2,int(number/2)):
	# if(number/x % 1.0 == 0):
		# if(funcs.is_prime(x)):
			# print x
		
x = 2
		
while(not funcs.is_prime(number)):
	if(number/x % 1.0 == 0):
		print x
		number = int(number/x)
		x = 2
	else:
		x+=1
		
print number