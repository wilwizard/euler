from __future__ import division
from sys import argv
import funcs
import math

script, limit = argv
limit=int(limit)

p_max=0
for p in range(limit):
    trips=0
    for x in range(1,int(.3*p)):
        y=(p-x)/2
        while math.hypot(x,y)>p-x-y:
            y-=1
        if math.hypot(x,y)==p-x-y:
            trips+=1
    p_max=max(trips,p_max)
    print p,p_max
