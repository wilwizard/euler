from __future__ import division
from sys import argv
import funcs

script, number = argv
number = int(number)

num=1
den=2
count=0
for i in range(number):
    if len(str(num+den))>len(str(den)):
        print str(num+den)+'/'+str(den)
        count+=1
    temp=num
    num=den
    den=temp+2*den
    
print count 