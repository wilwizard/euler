from __future__ import division
from sys import argv
import funcs
import fractions

def sum_squares(num):
    num = str(int(num))
    tot=0
    for n in num:
        tot+=int(n)**2
    return tot
    
script, limit = argv
limit = int(limit)
count = 0
num = 1

while num<limit:
    cur_val=num
    while True:
        #print cur_val
        cur_val = sum_squares(cur_val)
        if cur_val == 89 or cur_val == 1:
            break
    num+=1
    if cur_val==89:
        count+=1
    if num%100==0:
        print num
    #print cur_val
    
print 'count:', count