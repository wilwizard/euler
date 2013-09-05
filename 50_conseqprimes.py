from __future__ import division
from sys import argv
import funcs

script, number = argv
limit = int(number)
file=open('file.txt','w')
primes=[]
max_seq=[]
cur_max=0


for x in range(4000):
	if funcs.is_prime(x):
		primes.append(x)

for x in range(len(primes)):
    for y in range(x,len(primes)):
        file.write(str(x)+':'+str(y)+'\n')
        if funcs.is_prime(sum(primes[x:y])) and sum(primes[x:y])<limit:
			if cur_max<len(primes[x:y]):
				cur_max=len(primes[x:y])
				max_seq=primes[x:y]
				print sum(max_seq),cur_max,max_seq[0],max_seq[-1]
print '===='
print sum(max_seq),max_seq,len(max_seq)