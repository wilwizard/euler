from __future__ import division
from sys import argv
import funcs



script, limit = argv
limit=int(limit)+1
file=open('file.txt','w')
total=0
for pan in [list(x) for x in funcs.permu(range(limit))]:

    d=''.join(pan)
    d234=int(''.join(pan[1:4]))
    d345=int(''.join(pan[2:5]))
    d456=int(''.join(pan[3:6]))
    d567=int(''.join(pan[4:7]))
    d678=int(''.join(pan[5:8]))
    d789=int(''.join(pan[6:9]))
    d8910=int(''.join(pan[7:]))
   
   
    file.write(d+'\n')
    if d234%2!=0:
        continue
    if d345%3!=0:
        continue
    if d456%5!=0:
        continue
    if d567%7!=0:
        continue
    if d678%11!=0:
        continue
    if d789%13!=0:
        continue
    if d8910%17!=0:
        continue
    
    total+=int(d)
    print d
print total
    
       