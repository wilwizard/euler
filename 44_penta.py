from __future__ import division
from sys import argv
import funcs

script, limit = argv
limit=int(limit)
file = open('file.txt','w')

for k in range(1,limit):
    a1=range(1,k)
    a1.reverse()
    for j in a1:
        if funcs.is_penta(funcs.pentagonal(k)-funcs.pentagonal(j)) and funcs.is_penta(funcs.pentagonal(k)+funcs.pentagonal(j)):
            print funcs.pentagonal(k),funcs.pentagonal(j)
            
