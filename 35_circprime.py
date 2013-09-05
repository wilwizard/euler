from __future__ import division
from sys import argv
import funcs

script, limit = argv
file = open('file.txt', 'w')
limit = int(limit)
total=0

for num in xrange(2,limit):
    num = list(str(num))
    length = len(num)
    while funcs.is_prime(int(''.join(num))):
            temp=num.pop()
            num.insert(0,temp)
            length-=1
            if length==0:
                num = ''.join(num)
                file.write(num+'\n')
                total+=1
                break
print total
                