from __future__ import division
from sys import argv
import funcs
import fractions

script, num = argv
num=int(num)

#construct e
e=[2]
for k in range(1,int(num/3*2)+1):
    e+=[1,2*k,1]
print e

a=e[:num]
a.reverse()

total=fractions.Fraction(0)
for x in a:
    if total==0:
        total=fractions.Fraction(x)
    else:
        total=total.invert()+x
        
print fractions.Fraction(total)
print funcs.digitsum(total.numerator)