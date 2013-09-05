from __future__ import division
from sys import argv
import funcs

# script, limit = argv
# limit=int(limit)+1
file = open('file.txt','w')

#generate primes
primes=[]
for x in xrange(1000,10000):
    if funcs.is_prime(x):
        primes.append(x)
        
while primes:
    p=primes.pop(0)
    perms=[]
    perms.append(p)
    
    temp=primes[:]
    
    p_temp=list(str(p))
    p_temp.sort()
    p_temp=''.join(p_temp)
    
    for x in temp:
        x_temp=list(str(x))
        x_temp.sort()
        x_temp=''.join(x_temp)
        if p_temp==x_temp:
            perms.append(x)
            primes.remove(x)
    if len(perms)>2:
        #print perms
        diffs=[]
        for x in range(len(perms)-1):
            diffs.append(perms[x+1]-perms[x])
        for x in range(len(diffs)-1):
            if diffs[x]==diffs[x+1]:
                print perms,diffs
                print ''.join([str(x) for x in perms[1:]])