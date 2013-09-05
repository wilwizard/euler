from __future__ import division
from sys import argv
import funcs

script, limit = argv
limit=int(limit)
#file = open('file.txt','w')


for x in range(286,limit):
    if funcs.is_penta(funcs.triangle(x)) and funcs.is_hex(funcs.triangle(x)):
        print x,funcs.triangle(x)
