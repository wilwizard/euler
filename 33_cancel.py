from __future__ import division
from sys import argv
import funcs
import math

# script, number = argv
# number = int(number)
# x/y
total=1
for x in range(10,100):
    for y in range(x+1,100):
        y_array=funcs.num_to_array(y)
        x_array=funcs.num_to_array(x)
        shared_number=set(x_array)&set(y_array)
        #print x_array,y_array,shared_number
        if shared_number:
            x_array.remove(list(shared_number)[0])
            y_array.remove(list(shared_number)[0])
            x2=int(''.join([str(n) for n in list(x_array)]))
            y2=int(''.join([str(n) for n in list(y_array)]))
            if y2==0:
                continue
            #print x2,y2
            elif x2/y2==x/y and x%10!=0:
                total*=x/y
                print x,y
print total