from __future__ import division
from sys import argv
import funcs

script, limit = argv
file = open('file.txt', 'w')
limit = int(limit)
total=0


for num in xrange(10,limit):
    if not funcs.is_prime(num):
        continue
    num_array = list(str(num))
    temp=num_array[:]
    trunc_left=False
    trunc_right=False
    
    #truncate from right
    while len(temp)>0:
        if not funcs.is_prime(int(''.join(temp))):
            break
        else:
            temp.pop()
    if len(temp)==0:
        trunc_right=True
        
    #truncate from left   
    temp=num_array[:]
    while len(temp)>0:
        if not funcs.is_prime(int(''.join(temp))):
            break
        else:
            temp.pop(0)
    if len(temp)==0:
        trunc_left=True
        
    if trunc_right and trunc_left:
        print str(num)
        total+=num
        
print total