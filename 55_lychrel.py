from __future__ import division
from sys import argv
import funcs
import itertools 

def rev(num):
    array=list(str(num))
    array.reverse()
    return int(''.join(array))
   

script, limit = argv
limit=int(limit)+1
lych=0

for num in range(10,limit):
    iter=1
    temp=num+rev(num)
    while not funcs.is_pala(list(str(temp))):
        iter+=1
        if iter>50:
            lych+=1
            print num
            break
        temp=temp+rev(temp)
print lych