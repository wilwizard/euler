from __future__ import division
from sys import argv


def traverse(current_trail, 
    current_number = int(str(current_trail[-1])[2:])
            

    
tris=[]
squs=[]
pents=[]
hexs=[]
hepts=[]
octs=[]

x=1
n=1
while n<10000:
    n=int(x*(x+1)/2)
    if n>999 and n<10000 and str(n)[-2]!='0':
        tris.append(int(n))
    x+=1

x=1
n=1
while n<10000:
    n=int(x**2)
    if n>999 and n<10000 and str(n)[-2]!='0':
        squs.append(int(n))
    x+=1

x=1
n=1
while n<10000:
    n=int(x*(3*x-1)/2)
    if n>999 and n<10000 and str(n)[-2]!='0':
        pents.append(int(n))
    x+=1

x=1
n=1     
while n<10000:
    n=int(x*(2*x-1))
    if n>999 and n<10000 and str(n)[-2]!='0':
        hexs.append(int(n))
    x+=1

x=1
n=1    
while n<10000:
    n=int(x*(5*x-3)/2)
    if n>999 and n<10000 and str(n)[-2]!='0':
        hepts.append(int(n))
    x+=1

x=1
n=1 
while n<10000:
    n=x*(3*x-2)
    if n>999 and n<10000 and str(n)[-2]!='0':
        octs.append(int(n))
    x+=1
    
poly_array=[tris,squs,pents,hexs,hepts,octs]


#for start in poly_array[0]:
    
    
    #print traverse(start,[0,1,1,1,1,1])

    
    