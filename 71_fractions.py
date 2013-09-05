from __future__ import division
from sys import argv
import funcs
import fractions

script, limit = argv
limit=int(limit)
current_max=fractions.Fraction(0)

for n in range(limit,2,-1):
    x=int(n*3/7)
    if fractions.Fraction(x,n)<fractions.Fraction(3,7) and fractions.Fraction(x,n)>current_max:
        current_max=fractions.Fraction(x,n)
        print current_max
        
print 'FINAL ANSWER: ', current_max