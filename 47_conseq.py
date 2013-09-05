from __future__ import division
from sys import argv
import funcs

# script, limit = argv
# limit=int(limit)
#file = open('file.txt','w')


x=1
while True:
    print x+3,len(funcs.prime_facts(x+3))
    if len(funcs.prime_facts(x+3))<4:
        x+=4
        continue
    print x+2,len(funcs.prime_facts(x+2))
    if len(funcs.prime_facts(x+2))<4:
        x+=3
        continue
    print x+1,len(funcs.prime_facts(x+1))
    if len(funcs.prime_facts(x+1))<4:
        x+=2
        continue
    print x,len(funcs.prime_facts(x))
    if len(funcs.prime_facts(x))<4:
        x+=1
        continue
    print '==='
    print x
    break
    
def pf(num):
    temp=num
    facts=[]
    count=0
    x=2
    while temp>1 and count<4:
        if is_prime(x):
            while temp/x%1.0==0:
                temp//=x
                facts.append(x)
        x+=1
    return list(set(facts))