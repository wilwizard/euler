from __future__ import division
from sys import argv
import funcs
import itertools
import time

#97-122
script, filename = argv
file=open(filename,'r')
of=open('outfile.txt','w')
line=file.readline()



for key in itertools.product(['i','g','o','a','d','j','b','u','v','s','k'],repeat=3):

    key = [ord(x) for x in list(key)]
    
    code=[int(i) for i in line.split(',')]
    message=[]
    for i in range(len(code)):
        message.append(chr(code[i]^key[i%3]))
    
    
    of.write(''.join(message))
    of.write(str(key)+'\n')            

    

#[103, 111, 100]
#'god'