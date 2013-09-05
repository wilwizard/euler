from __future__ import division
from sys import argv
import funcs

# script, limit = argv
# limit=int(limit)
#file = open('file.txt','w')

"""
n=prime+2*a^2
"""
x=0
while 1:
    x+=1
    n=2*x+1
    if funcs.is_prime(n):
        print str(n)+':prime'
        continue
    a=1
    while not funcs.is_prime(n-2*a**2):
        a+=1
        if 2*a**2>n:
            print '***'
            print n
            quit()
    print n,a
    
