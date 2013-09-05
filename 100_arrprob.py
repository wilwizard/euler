from __future__ import division
from sys import argv
import funcs
import fractions

def test(b,r):
    return b**2-b-2*b*r-r**2+r
    
b=707106781187
r=10**12-b
t=test(b,r)
    
while 1:
    if t>0:
        r+=1
    if t<0:
        b+=1
    #t=test(b,r)
    print b,r,t

print b