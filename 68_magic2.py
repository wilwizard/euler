from __future__ import division
from sys import argv
import funcs
import fractions
import itertools

outer_numbers = [6,7,8,9,10]
inner_numbers = [1,2,3,4,5]

magic = [[0,0,0],
         [0,0,0],
         [0,0,0],
         [0,0,0],
         [0,0,0]]

for y in itertools.permutations(outer_numbers):

    magic[0][0]=y[0]
    magic[1][0]=y[1]
    magic[2][0]=y[2]
    magic[3][0]=y[3]
    magic[4][0]=y[4]    
    
    for x in itertools.permutations(inner_numbers):
        
        magic[0][1]=x[0]
        magic[4][2]=x[0]
        
        magic[1][1]=x[1]
        magic[0][2]=x[1]
                   
        magic[2][1]=x[2]
        magic[1][2]=x[2]
                   
        magic[3][1]=x[3]
        magic[2][2]=x[3]
        
        magic[4][1]=x[4]
        magic[3][2]=x[4]
        
        if sum(magic[0])==sum(magic[1])==sum(magic[2])==sum(magic[3])==sum(magic[4]):
            print magic
    
    
    
# 6531031914842725